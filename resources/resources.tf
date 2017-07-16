provider "aws" {
  region  = "${var.region}"
  profile = "${var.profile}"
}

data "aws_subnet_ids" "humblebee_subnet_ids" {
  vpc_id = "${var.vpc_id}"
}

data "aws_subnet" "humblebee_subnet" {
  count = "${length(data.aws_subnet_ids.humblebee_subnet_ids.ids)}"
  id    = "${data.aws_subnet_ids.humblebee_subnet_ids.ids[count.index]}"
}

data "aws_ami" "amazon_linux" {
  most_recent = true

  filter {
    name   = "owner-alias"
    values = ["amazon"]
  }

  filter {
    name = "name"
    values = ["amzn-ami-hvm-*-gp2"]
  }

  filter {
    name = "architecture"
    values = ["x86_64"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "state"
    values = ["available"]
  }
}

resource "aws_ebs_volume" "humblebee_volume" {
  count             = "${var.count}"
  availability_zone = "${element(data.aws_subnet.humblebee_subnet.*.availability_zone, count.index)}"
  encrypted         = true
  tags {
    Name = "Humblebee"
  }
}

resource "aws_volume_attachment" "humblebee_attachment" {
  count       = "${var.count}"
  device_name = "/dev/sdz"
  volume_id   = "${element(aws_ebs_volume.humblebee_volume.*.id, count.index)}"
  instance_id = "${element(aws_instance.humblebee_instance.*.id, count.index)}"
}

resource "aws_instance" "humblebee_instance" {
  count                       = "${var.count}"
  ami                         = "${data.aws_ami.amazon_linux.id}"
  instance_type               = "t2.micro"
  associate_public_ip_address = false
  subnet_id                   = "${element(data.aws_subnet_ids.humblebee_subnet_ids.ids, count.index)}"
  tags {
    Name = "HumbleBee"
  }
}

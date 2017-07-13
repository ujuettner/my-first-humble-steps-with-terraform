provider "aws" {
  region  = "${var.region}"
  profile = "${var.profile}"
}

data "aws_ami" "amazon_linux" {
  most_recent = true

  filter {
    name = "architecture"
    values = ["x86_64"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "owner-alias"
    values = ["amazon"]
  }
}

resource "aws_instance" "humblebee" {
  ami           = "${data.aws_ami.amazon_linux.id}"
  instance_type = "t2.micro"

  tags {
    Name = "HumbleBee"
  }
}

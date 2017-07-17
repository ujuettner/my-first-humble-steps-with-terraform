provider "aws" {
  region  = "${var.region}"
  profile = "${var.profile}"
}

resource "aws_s3_bucket" "terraform_shared_state" {
  bucket = "my-first-humble-steps-with-terraform-${lower(var.profile)}"
  acl    = "private"

  versioning {
    enabled = true
  }

  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_dynamodb_table" "terraform_shared_state_lock" {
  name           = "my-first-humble-steps-with-terraform-${lower(var.profile)}-lock"
  read_capacity  = 5
  write_capacity = 5
  hash_key       = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }
}

output "terraform_shared_state_bucket" {
  value = "${aws_s3_bucket.terraform_shared_state.id}@${aws_s3_bucket.terraform_shared_state.region}"
}

output "terraform_shared_state_lock_table" {
  value = "${aws_dynamodb_table.terraform_shared_state_lock.id}"
}

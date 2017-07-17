terraform {
  backend "s3" {
    bucket         = "my-first-humble-steps-with-terraform-staging"
    key            = "staging/terraform.tfstate"
    region         = "ca-central-1"
    encrypt        = "true"
    dynamodb_table = "my-first-humble-steps-with-terraform-staging-lock"
  }
}

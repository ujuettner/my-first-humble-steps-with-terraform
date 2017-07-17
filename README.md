# my-first-humble-steps-with-terraform
Code for
[this](https://dumb-tiger.blogspot.de/2017/07/first-humble-steps-with-terraform.html)
blog post.

Add a profile to your `~/.aws/credentials`:
```
[STAGING]
aws_access_key_id=...
aws_secret_access_key=...
```
```
$ git clone
https://github.com/ujuettner/my-first-humble-steps-with-terraform
$ cd my-first-humble-steps-with-terraform/staging
```
Edit `terraform.tfvars` to reflect your environment.

Get the module and initialize the remote state:
```
$ terraform get
$ terraform init
```
Perform a dry run to check for errors and to see, what would be done:
```
$ terraform plan
```
Apply the provisioning:
```
$ terraform apply
```
Final cleanup:
```
$ terraform destroy
```

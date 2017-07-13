module "resources" {
  source  = "../resources"

  region  = "${var.region}"
  profile = "${var.profile}"
}

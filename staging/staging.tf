module "resources" {
  source  = "../resources"

  region  = "${var.region}"
  profile = "${var.profile}"
  vpc_id  = "${var.vpc_id}"
  count   = "${var.count}"
}

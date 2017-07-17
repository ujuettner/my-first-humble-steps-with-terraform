output "public_ips" {
  value = ["${aws_instance.humblebee_instance.*.public_ip}"]
}

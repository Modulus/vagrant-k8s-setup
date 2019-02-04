def test_verify_docker_service_is_running(host):
    user = host.user("ubuntu")

    assert user.name == "ubuntu"
    assert user.uid == 1001

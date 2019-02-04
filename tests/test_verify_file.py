def test_verify_file(host):
    text_file = host.file("/home/vagrant/file.txt")

    assert text_file.exists 
    assert text_file.is_file 

    assert text_file.user == "ubuntu"
    assert text_file.uid == 1001
    assert oct(text_file.mode) == '0o444'
    assert text_file.contains("I'm on a horse!")
from project import parse_args, capture_images, create_gif, gif_resolution

def test_default_args():
    args = parse_args([])
    assert args.images == 10
    assert args.time == 2.0
    assert args.display is True
    assert args.size == "medium"

def test_parse_args():
    parser = parse_args(["--images", "5", "--time", "2", "--size", "small"])
    assert parser.images == 5
    assert parser.time == 2.0
    assert parser.size == "small"

def test_valid_time():
    assert parse_args(["--time", "0.5"]).time == 0.5
    assert parse_args(["--time", "2"]).time == 2.0
    assert parse_args(["--time", "60"]).time == 60.0

def test_gif_resolution():
    assert gif_resolution("small") == (320, 240)
    assert gif_resolution("medium") == (640, 480)
    assert gif_resolution("xl") == (1280, 960)

from app.api_interact import ApiInterct
from app.criptography import Criptography


def main():
    api_interact = ApiInterct()
    criptography = Criptography()

    api_interact.get_info()
    criptography.descriptography()
    criptography.resume_sha1()
    api_interact.post_info()


if __name__ == "__main__":
    main()

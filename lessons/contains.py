

# When put together, it should look like this 

def main() -> None:
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davidson"]))


def contains(needle: str, haystack: list[str]) -> bool:
    for item in haystack:
        if item == needle:
            return True
        return False


if __name__ == "__main__":
    main()


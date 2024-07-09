calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    for str in list_to_search:
        if string.lower() == str.lower():
            return True
    return False

print(string_info("AlasSka"))
print(is_contains("HiadD", ["hiadd", "dasdas", 23]))
print(is_contains("Fleks", ["FLEKs"]))
print(is_contains("DOM", ["DOM"]))
print(calls)

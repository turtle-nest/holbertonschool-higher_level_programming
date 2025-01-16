#!/usr/bin/python3
print(
    "".join(
        "{:c}".format(c if i % 2 == 0 else c - 32)
        for i, c in enumerate(range(122, 96, -1))
    ),
    end=""
)

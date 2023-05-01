from pathlib import Path

try:
    path = Path('./qoran.txt')

    qoran_text = path.read_text()

    The_count = qoran_text.count('The')
    the_count = qoran_text.count('the')
    just_the_count = qoran_text.lower().count('the ')

    print(
        (3 * '\n'),
        "'The' counter:",
        The_count,
    )

    print(
        ('\n'),
        "'the' counter:",
        the_count,
        (3 * '\n'),
    )

    print(
        "'the ' counter:",
        just_the_count
    )
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

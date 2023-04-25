from pathlib import Path

path = Path('./qoran.txt')

qoran_text = path.read_text()

The_count = qoran_text.count('The')
the_count = qoran_text.count('the')
just_the_count = qoran_text.lower().count('the ')

print(
    "'The' counter:",
    The_count
)

print(
    "'the' counter:",
    the_count
)

print(
    "'the ' counter:",
    just_the_count
)

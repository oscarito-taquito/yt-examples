# Example on how to format variables
# within a triple-quoted string

age = 99
income = 123456.78
bonus = 0.05675

msg = f"""I am a {age} years old
My income is ${'{:,.2f}'.format(income)}
with an annual bonus of {bonus:.2%}."""

print(msg)

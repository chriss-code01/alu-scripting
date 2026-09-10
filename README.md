# Regular Expressions

This project contains Ruby scripts that use regular expressions with the Oniguruma library.

## Tasks

The project covers different regular expression concepts:

- Simply matching `School`
- Repetition tokens
- Matching the beginning and end of strings
- Matching a 10-digit phone number
- Extracting capital letters
- Extracting information from TextMe log messages

## Files

- `0-simply_match_school.rb` - Matches the word `School`
- `1-repetition_token_0.rb` - Uses a repetition range
- `2-repetition_token_1.rb` - Uses the `?` repetition token
- `3-repetition_token_2.rb` - Uses the `+` repetition token
- `4-repetition_token_3.rb` - Uses the `*` repetition token
- `5-beginning_and_end.rb` - Matches strings beginning with `h`, one character, and ending with `n`
- `6-phone_number.rb` - Matches a 10-digit phone number
- `7-OMG_WHY_ARE_YOU_SHOUTING.rb` - Extracts uppercase letters
- `8-textme.rb` - Extracts sender, receiver, and flags from TextMe messages

## Usage

Each script accepts one argument.

Example:

```bash
./0-simply_match_school.rb "Best School"

""" Мой гайд по регуляркам"""
# import re
# Мы используем в регулярных выражениях префикс 'r' (raw string) чтобы не происходило вещей типа "\\\\" для поиска
# одной косой черты ('\\\\' = '\\' в Python = '\' в обычной жизни).
# Вместо этого можно использовать r'\\' (что для Python так же будет '\\', т.е. просто '\'.
# Цитата -- "it’s highly recommended that you use raw strings for all but the simplest expressions".
"""
########################################################################################################################
###################################################### Функции re: #####################################################
########################################################################################################################
"""
#
# re.compile(pattern, flags=0) -- позволяет сохранить паттерн для многократного использования и экономии ресурсов.
#
# re.escape(pattern) -- если мы используем строку в качестве паттерна, то escape делает эту строку "безопасной"
# (например, в адресе сайта экранирует точки, чтобы они искались как точки, а не как спец. символы).
#
# re.findall(pattern, string, flags=0) -- возвращает список объектов или кортежей. Поиск по группам?..
#
# re.finditer(pattern, string, flags=0) -- возвращает генератор, который выдаёт все совпадения.
#
# re.fullmatch(pattern, string, flags=0) -- checks for entire string to be a match.
#
# re.match(pattern, string, flags=0) -- checks for a match only at the beginning of the string.
#
# re.purge() -- "Clear the regular expression cache", что бы это не значило.
#
# re.search(pattern, string, flags=0) -- возвращает первое совпадение по паттерну из строки где угодно
# (не только в начале).
#
# re.split(pattern, string, maxsplit=0, flags=0) -- возвращает список деления строки по паттерну.
#
# re.sub(pattern, repl, string, count=0, flags=0) -- для замены совпадений паттерна в строке на repl.
# Если совпадений нет, возвращает изначальную строку. Много нюансов использования!
#
# re.subn(pattern, repl, string, count=0, flags=0) -- То же, что и re.sub(), но возвращает кортеж
# (new_string, number_of_subs_made).
#
# re.template(pattern, flags) -- непонятно.
#
"""
########################################################################################################################
###################################################### Исключения ######################################################
########################################################################################################################
"""
# Можно вызвать исключение, если со строкой что-то не так.
#
"""
########################################################################################################################
######################################################## Флаги: ########################################################
########################################################################################################################
"""
# re.A = re.ASCII = (?a)
# По умолчанию поиск ведётся в Unicode, этот флаг делает \w, \W, \b, \B, \d, \D, \s и \S ASCII-only.
#
# re.DEBUG -- что-то непонятное про дебаггинг.
#
# re.I = re.IGNORECASE = (?i) -- не обращает внимания на регистр букв.
#
# re.L = re.LOCALE = (?L) -- Флаг локалей (только для 8-битного поиска!).
#
# re.M = re.MULTILINE = (?m) -- #todo
# When specified, the pattern character '^' matches at the beginning of the string and at the beginning of each line
# (immediately following each newline); and the pattern character '$' matches at the end of the string and at the end of
# each line (immediately preceding each newline). By default, '^' matches only at the beginning of the string,
# and '$' only at the end of the string and immediately before the newline (if any) at the end of the string.

# re.NOFLAG -- Используется для создания своих функций с флагами:
# def myfunc(text, flag=re.NOFLAG):
#    return re.match(text, flag)

# re.S = re.DOTALL = (?s) -- С этим флагом точка ('.') заменяет и символ новой строки ('\n').

# re.X = re.VERBOSE = (?x) -- #todo
# Даёт возможность визуально разбивать регулярные выражения и добавлять к ним комментарии.
#
# Whitespace within the pattern is ignored, except when in a character class, or when preceded by an unescaped
# backslash, or within tokens like '*?', '(?:' or '(?P<...>'. For example, '(? :' and '* ?' are not allowed.
# When a line contains a '#' that is not in a character class and is not preceded by an unescaped backslash,
# all characters from the leftmost such '#' through the end of the line are ignored.

# Ниже a и b равны:
# a = re.compile(r"""\d +  # the integral part
#                    \.    # the decimal point
#                    \d *  # some fractional digits""", re.X)
# b = re.compile(r"\d+\.\d*")
#
"""
########################################################################################################################
############################################ Методы объектов Match и Pattern ###########################################
########################################################################################################################
"""
# Since match() and search() return None when there is no match, you can test whether there was a match
# with a simple if statement:
#
# match = re.search(pattern, string)
# if match:
#     process(match)
#
# Match.expand(template)
# Return the string obtained by doing backslash substitution on the template string template, as done by the sub()
# method. Escapes such as \n are converted to the appropriate characters,
# and numeric backreferences (\1, \2) and named backreferences (\g<1>, \g<name>) are replaced
# by the contents of the corresponding group.
#
# Unmatched groups are replaced with an empty string.
#
# Match.group([group1, ...])
# Returns one or more subgroups of the match. If there is a single argument, the result is a single string;
# if there are multiple arguments, the result is a tuple with one item per argument.
# Without arguments, group1 defaults to zero (the whole match is returned). If a groupN argument is zero,
# the corresponding return value is the entire matching string; if it is in the inclusive range [1..99],
# it is the string matching the corresponding parenthesized group. If a group number is negative or larger than
# the number of groups defined in the pattern, an IndexError exception is raised.
# If a group is contained in a part of the pattern that did not match, the corresponding result is None.
# If a group is contained in a part of the pattern that matched multiple times, the last match is returned.
# >>>
#
# m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
#
# m.group(0)       # The entire match
# 'Isaac Newton'
#
# m.group(1)       # The first parenthesized subgroup.
# 'Isaac'
#
# m.group(2)       # The second parenthesized subgroup.
# 'Newton'
#
# m.group(1, 2)    # Multiple arguments give us a tuple.
# ('Isaac', 'Newton')
#
# If the regular expression uses the (?P<name>...) syntax, the groupN arguments may also be
# strings identifying groups by their group name. If a string argument is not used as a group name in the pattern,
# an IndexError exception is raised.
#
# A moderately complicated example:
# >>>
#
# m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
#
# m.group('first_name')
# 'Malcolm'
#
# m.group('last_name')
# 'Reynolds'
#
# Named groups can also be referred to by their index:
# m.group(1)
# 'Malcolm'
#
# m.group(2)
# 'Reynolds'
#
# If a group matches multiple times, only the last match is accessible:
# m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times.
#
# m.group(1)                        # Returns only the last match.
# 'c3'
#
# Match.__getitem__(g)
# This is identical to m.group(g). This allows easier access to an individual group from a match:
# m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
#
# m[0]       # The entire match
# 'Isaac Newton'
#
# m[1]       # The first parenthesized subgroup.
# 'Isaac'
#
# m[2]       # The second parenthesized subgroup.
# 'Newton'
#
# Named groups are supported as well:
# m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Isaac Newton")
#
# m['first_name']
# 'Isaac'
#
# m['last_name']
# 'Newton'
#
# Match.groups(default=None)
# Return a tuple containing all the subgroups of the match, from 1 up to however many groups are in the pattern.
# The default argument is used for groups that did not participate in the match; it defaults to None.
#
# For example:
# m = re.match(r"(\d+)\.(\d+)", "24.1632")
#
# m.groups()
# ('24', '1632')
#
# If we make the decimal place and everything after it optional, not all groups might participate in the match.
# These groups will default to None unless the default argument is given:
# m = re.match(r"(\d+)\.?(\d+)?", "24")
#
# m.groups()      # Second group defaults to None.
# ('24', None)
#
# m.groups('0')   # Now, the second group defaults to '0'.
# ('24', '0')
#
# Match.groupdict(default=None)
# Return a dictionary containing all the named subgroups of the match, keyed by the subgroup name.
# The default argument is used for groups that did not participate in the match; it defaults to None. For example:
# m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
#
# m.groupdict()
# {'first_name': 'Malcolm', 'last_name': 'Reynolds'}
#
# Match.start([group])
# Match.end([group])
# Return the indices of the start and end of the substring matched by group; group defaults to zero
# (meaning the whole matched substring). Return -1 if group exists but did not contribute to the match.
# For a match object m, and a group g that did contribute to the match, the substring matched by group g
# (equivalent to m.group(g)) is
#
# m.string[m.start(g):m.end(g)]
#
# Note that m.start(group) will equal m.end(group) if group matched a null string. For example,
# after m = re.search('b(c?)', 'cba'), m.start(0) is 1, m.end(0) is 2, m.start(1) and m.end(1) are both 2,
# and m.start(2) raises an IndexError exception.
#
# An example that will remove remove_this from email addresses:
# email = "tony@tiremove_thisger.net"
#
# m = re.search("remove_this", email)
#
# email[:m.start()] + email[m.end():]
# 'tony@tiger.net'
#
# Match.span([group])
#
# For a match m, return the 2-tuple (m.start(group), m.end(group)). Note that if group did not contribute to the match,
# this is (-1, -1). group defaults to zero, the entire match.
#
# Match.pos
# The value of pos which was passed to the search() or match() method of a regex object.
# This is the index into the string at which the RE engine started looking for a match.
#
# Match.endpos
# The value of endpos which was passed to the search() or match() method of a regex object.
# This is the index into the string beyond which the RE engine will not go.
#
# Match.lastindex
# The integer index of the last matched capturing group, or None if no group was matched at all.
# For example, the expressions (a)b, ((a)(b)), and ((ab)) will have lastindex == 1 if applied to the string 'ab',
# while the expression (a)(b) will have lastindex == 2, if applied to the same string.
#
# Match.lastgroup
# The name of the last matched capturing group, or None if the group didn’t have a name, or if no group was matched
# at all.
#
# Match.re
# The regular expression object whose match() or search() method produced this match instance.
#
# Match.string
# The string passed to match() or search().
#
# Added support of copy.copy() and copy.deepcopy(). Match objects are considered atomic.
#
# Pattern.search(string[, pos[, endpos]])
# Scan through string looking for the first location where this regular expression produces a match, and return
# a corresponding match object. Return None if no position in the string matches the pattern; note that
# this is different from finding a zero-length match at some point in the string.
#
# The optional second parameter pos gives an index in the string where the search is to start; it defaults to 0.
# This is not completely equivalent to slicing the string; the '^' pattern character matches at the real
# beginning of the string and at positions just after a newline, but not necessarily at the index
# where the search is to start.
#
# The optional parameter endpos limits how far the string will be searched; it will be as if the string is
# endpos characters long, so only the characters from pos to endpos - 1 will be searched for a match.
# If endpos is less than pos, no match will be found; otherwise, if rx is a compiled regular expression object,
# rx.search(string, 0, 50) is equivalent to rx.search(string[:50], 0).
#
# pattern = re.compile("d")
#
# pattern.search("dog")     # Match at index 0
# <re.Match object; span=(0, 1), match='d'>
#
# pattern.search("dog", 1)  # No match; search doesn't include the "d"
#
# Pattern.match(string[, pos[, endpos]])
# If zero or more characters at the beginning of string match this regular expression, return a corresponding
# match object. Return None if the string does not match the pattern; note that this is different from a
# zero-length match.
#
# The optional pos and endpos parameters have the same meaning as for the search() method.
#
# pattern = re.compile("o")
#
# pattern.match("dog")      # No match as "o" is not at the start of "dog".
#
# pattern.match("dog", 1)   # Match as "o" is the 2nd character of "dog".
# <re.Match object; span=(1, 2), match='o'>
#
# If you want to locate a match anywhere in string, use search() instead (see also search() vs. match()).
#
# Pattern.fullmatch(string[, pos[, endpos]])
# If the whole string matches this regular expression, return a corresponding match object.
# Return None if the string does not match the pattern; note that this is different from a zero-length match.
# The optional pos and endpos parameters have the same meaning as for the search() method.
#
# pattern = re.compile("o[gh]")
#
# pattern.fullmatch("dog")      # No match as "o" is not at the start of "dog".
# pattern.fullmatch("ogre")     # No match as not the full string matches.
# pattern.fullmatch("doggie", 1, 3)   # Matches within given limits.
# <re.Match object; span=(1, 3), match='og'>
#
#
# Pattern.split(string, maxsplit=0)
# Identical to the split() function, using the compiled pattern.
#
# Pattern.findall(string[, pos[, endpos]])
# Similar to the findall() function, using the compiled pattern, but also accepts optional pos and endpos parameters
# that limit the search region like for search().
#
# Pattern.finditer(string[, pos[, endpos]])
# Similar to the finditer() function, using the compiled pattern, but also accepts optional pos and endpos parameters
# that limit the search region like for search().
#
# Pattern.sub(repl, string, count=0)
# Identical to the sub() function, using the compiled pattern.
#
# Pattern.subn(repl, string, count=0)
# Identical to the subn() function, using the compiled pattern.
#
# Pattern.flags
# The regex matching flags. This is a combination of the flags given to compile(), any (?...) inline flags
# in the pattern, and implicit flags such as UNICODE if the pattern is a Unicode string.
#
# Pattern.groups
# The number of capturing groups in the pattern.
#
# Pattern.groupindex
# A dictionary mapping any symbolic group names defined by (?P<id>) to group numbers. The dictionary is empty
# if no symbolic groups were used in the pattern.
#
# Pattern.pattern
# The pattern string from which the pattern object was compiled.
# Added support of copy.copy() and copy.deepcopy(). Compiled regular expression objects are considered atomic.
#
"""
########################################################################################################################
###################################################### Спецсимволы #####################################################
########################################################################################################################
"""
# . -- Любой символ

# ^ -- Начало Строки, вместе с флагом MULTILINE также начало подстрочек.
# # $ --
# Matches the end of the string or just before the newline at the end of the string, вместе с флагом MULTILINE
# также matches before a newline.foo matches both ‘foo’ and ‘foobar’, while the regular expression foo$ matches
# only ‘foo’. More interestingly, searching for foo.$ in 'foo1\nfoo2\n' matches ‘foo2’ normally,
# but ‘foo1’ in MULTILINE mode; searching for a single $ in 'foo\n' will find two (empty) matches: one
# just before the newline, and one at the end of the string.
#
# # * -- Предыдущий элемент любое количество раз. Выражение ab* значит "a и сколько угодно (0+) b".
#
# # + -- Предыдущий элемент 1 или больше раз. Выражение ab+ значит "ab, где b может быть сколько угодно, главное не 0".
#
# # ? -- Предыдущий элемент 0 или 1 раз. Выражение 'ab?' значит "a и либо 1 либо 0 раз b", т.е. либо ‘a’ либо ‘ab’.
#
# # *?, +?, ?? --
# The '*', '+', and '?' quantifiers are all greedy; they match as much text as possible. Sometimes this behaviour
# isn’t desired; if the RE <.* > is matched against '<a> b <c>', it will match the entire string, and not just
# '<a>'. Adding ? after the quantifier makes it perform the match in non - greedy or minimal fashion; as few
# characters as possible will be matched. Using the RE <.* ? > will match only '<a>'.
#
# # *+, ++, ?+ --
# Like the '*', '+', and '?' quantifiers, those where '+' is appended also match as many times as possible.
# However, unlike the true greedy quantifiers, these do not allow back - tracking when the expression following it
# fails to match. These are known as possessive quantifiers. For example, a * a will match 'aaaa' because the a * will
# match all 4 'a' s, but, when the final 'a' is encountered, the expression is backtracked so that in the end
# the a * ends up matching 3 'a' s total, and the fourth 'a' is matched by the final 'a'. However, when a * +a is used
# to match 'aaaa', the a * + will match all 4 'a', but when the final 'a' fails to find any more characters to match,
# the expression cannot be backtracked and will thus fail to match.
# То есть 'x*+' == '(?>x*)', 'x++' == '(?>x+)' и 'x?+' == '(?>x?)'.
#
# # {m} -- Предыдущий элемент должен быть ровно m число раз. Выражение 'a{6}' значит 'aaaaaa', но не 'aaaaa'.
#
# # {m, n} --
# Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many
# repetitions as possible.For example, a {3, 5} will match from 3 to 5 'a' characters.
# Omitting m specifies a lower bound of zero, and omitting n specifies an infinite upper bound.
# As an example, 'a{4, }b' will match 'aaaab' or a thousand 'a' characters followed by a 'b', but not 'aaab'.
# The comma may not be omitted or the modifier would be confused with the previously described form.
#
# # {m, n}? --
# Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as few
# repetitions as possible.This is the non - greedy version of the previous quantifier. For example, on the
# 6 - character string 'aaaaaa', a {3, 5} will match 5 'a' characters, while a{3, 5}? will only match 3 characters.
#
# # {m, n} + --
# Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many
# repetitions as possible without establishing any backtracking points.This is the possessive version of the
# quantifier above.For example, on the 6 - character string 'aaaaaa', a {3, 5} + aa attempt to match 5
# 'a' characters, then, requiring 2 more 'a' s, will need more characters than available and thus fail,
# while a{3, 5}aa will match with a{3, 5} capturing 5, then 4 'a's by backtracking and then the final 2 'a's are
# matched by the final aa in the pattern.x{m, n}+ is equivalent to (? > x{m, n}).
#
#
# # \ -- Escape-символ
#
# # [] -- Набор символов. В том числе:
# # -Просто допустимые символы (выражению '[amk]' соответствует 'a', 'm' или 'k').
# -Ranges of characters can be indicated by giving two characters and separating them by a '-', for example [a-z] will
# match any lowercase ASCII letter, [0-5][0-9] will match all the two-digits numbers from 00 to 59, and [0-9A-Fa-f] will
# match any hexadecimal digit.If - is escaped (e.g.[a\-z]) or if it’s placed as the first or last character
# (e.g.[-a] or[a-]), it will match a literal '-'.
#
# -Special characters lose their special meaning inside sets. For example, [(+ *)] will match any of the literal
# characters '(', '+', '*', or ')'.
#
# -Character classes such as \w or \S (defined below) are also accepted inside a set, although the characters they match
# depends on whether ASCII or LOCALE mode is in force.
#
# -Characters that are not within a range can be matched by complementing the set. If the first character of the set \
# is '^', all the characters that are not in the set will be matched. For example, [ ^ 5] will match any character
# except '5', and [ ^ ^] will match any character except '^'. ^ has no special meaning if it’s not the first character \
# in the set.
#
# -To match a literal ']' inside a set, precede it with a backslash, or place it at the beginning of the set.
# Например, both '[()[\]{}]' and '[]()[{}]' will match ], as well as [, {}, and ().
#
# -Support of nested sets and set operations as in Unicode Technical Standard No.18 might be added in the future.
# # This would change the syntax, so to facilitate this change a FutureWarning will be raised in ambiguous cases
# # for the time being. That includes sets starting with a literal '[' or containing literal character sequences '--',
# # '&&', '~~', and '||'. To avoid a warning escape them with a backslash.
#
# FutureWarning is raised if a character set contains constructs that will change semantically in the future.
#
# # | --
# A | B, where A and B can be arbitrary REs, creates a regular expression that will match either A or B.
# An arbitrary number of REs can be separated by the '|' in this way.
# This can be used inside groups (see below) as well.
# As the target string is scanned, REs separated by '|' are tried from left to right. When one pattern completely
# matches, that branch is accepted. This means that once A matches, B will not be tested further,
# even if it would produce a longer overall match. In other words, the '|' operator is never greedy.
# To match a literal '|', use \ |, or enclose it inside a character class , as in[|].
#
#
# # (...) --
# Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group;
# the contents of a group can be retrieved after a match has been performed, and can be matched later in the string with
# the \number special sequence, described below. To match the literals '(' or ')', use \( or  \), or enclose them
# inside a character class: [(], [)].
#
# # (?...) --
# This is an extension notation (a '?' following a '(' is not meaningful otherwise). The first character after the '?'
# determines what the meaning and further syntax of the construct is. Extensions usually do not create a new group;
# (?P < name >...) is the only exception to this rule. Following are the currently supported extensions.
#
# # (?aiLmsux) -- Можно включить флаги в само регулярное выражение: (?флаг(и)) должны стоять первыми в выражении!
#
# # (?:...) --
# A non - capturing version of regular parentheses.- Matches whatever regular expression is inside
# the parentheses, but the substring matched by the group cannot be retrieved after performing a match or referenced
# later in the pattern.
#
# # (?aiLmsux-imsx:...) --
# (Zero or more letters from the set 'a', 'i', 'L', 'm', 's', 'u', 'x', optionally followed by '-' followed by
# one or more letters from the 'i', 'm', 's', 'x'.)
# The letters set or remove the corresponding flags: re.A(ASCII - only matching), re.I(ignore case),
# re.L(locale dependent), re.M(multi - line), re.S(dot matches all), re.U(Unicode matching), and re.X(verbose), for
# the part of the expression.(The flags are described in Module Contents.)
#
# The letters 'a', 'L' and 'u' are mutually exclusive when used as inline flags,
# so they can’t be combined or follow '-'.
# Instead, when one of them appears in an inline group, it overrides the matching mode in the enclosing group.
# In Unicode patterns(?a: ...) switches to ASCII - only matching, and (?u:...) switches to Unicode matching(default).
# In byte pattern(?L: ...) switches to locale depending matching,
# and (?a:...) switches to ASCII - only matching(default).
# This override is only in effect for the narrow inline group, and the original matching mode is restored outside of
# the group.
#
# The letters 'a', 'L' and 'u' also can be used in a group.
#
# # (? >...) --
# Attempts to match... as if it was a separate regular expression, and if successful, continues to match the rest
# of the pattern following it. If the subsequent pattern fails to match, the stack can only be unwound to a point
# before the (? >...) because once exited, the expression, known as an atomic group, has thrown away all stack points
# within itself.Thus, (? >.* ).would never match anything because first the.* would match all characters possible, then,
# having nothing left to match, the final.would fail to match.Since there are no stack points saved in the Atomic Group,
# and there is no stack point before it, the entire expression would thus fail to match.
#
# # (?P < name >...) --
# Similar to regular parentheses, but the substring matched by the group is accessible via the symbolic group name name.
# Group names must be valid Python identifiers, and each group name must be defined only once within a RE.
# A symbolic group is also a numbered group, just as if the group were not named.
#
# Named groups can be referenced in three contexts. If the pattern is (?P < quote >['"]).*?(?P=quote) '
# (i.e. matching a string quoted with either single or double quotes):
#
# Context of reference to group “quote” -- Ways to reference it
#
# in the same pattern itself:
# (?P=quote)( as shown)
# \1
#
# when processing match object m:
# m.group('quote')
# m.end('quote')(etc.)
#
# in a string passed to the repl argument of re.sub():
# \g <quote>
# \g <1>
# \1
#
# Deprecated: Group name containing characters outside the ASCII range(b'\x00' - b'\x7f') in bytes patterns.
#
# # (?P = name) --
# A backreference to a named group; it matches whatever text was matched by the earlier group named name.
#
# # (?  # ...) --
# A comment; the contents of the parentheses are simply ignored.
#
# # (?=...) --
# Matches if ... matches next, but doesn’t consume any of the string. This is called a lookahead assertion.
# For example, Isaac(?=Asimov) will match 'Isaac ' only if it’s followed by 'Asimov'.
#
# # (?!...) --
# Matches if ... doesn’t match next. This is a negative lookahead assertion. For example, Isaac(?!Asimov) will match
# 'Isaac ' only if it’s not followed by 'Asimov'.
#
# # (? <= ...) --
# Matches if the current position in the string is preceded by a match for ... that ends at the current position.
# This is called a positive lookbehind assertion.(? <= abc)def will find a match in 'abcdef',
# since the lookbehind will back up 3 characters and check if the contained pattern matches. The contained pattern must
# only match strings of some fixed length, meaning that abc or a | b are allowed, but a * and a {3, 4} are not.
# Note that patterns which start with positive lookbehind assertions will not match at the beginning of
# the string being searched; you will most likely want to use the search() function rather than the match() function:
#
# import re
# m = re.search('(?<=abc)def', 'abcdef')
# m.group(0)
# 'def'
#
# This example looks for a word following a hyphen:
# m = re.search(r'(?<=-)\w+', 'spam-egg')
# m.group(0)
# 'egg'
#
# Added support for group references of fixed length.
#
# # (? < !...)
# Matches if the current position in the string is not preceded by a match for ....
# This is called a negative lookbehind assertion. Similar to positive lookbehind assertions,
# the contained pattern must only match strings of some fixed length.
# Patterns which start with negative lookbehind assertions may match at the beginning of the string being searched.
#
# # (?(id/name)yes - pattern | no - pattern)
# Will try to match with yes-pattern if the group with given id or name exists, and with no-pattern if it doesn’t.
# No-pattern is optional and can be omitted.
# For example, ( < )?(\w+ @ \w+(?:\.\w +)+)(?(1) > | $) is a poor email matching pattern, which will match with
# '<user@host.com>' as well as 'user@host.com', but not with '<user@host.com' nor 'user@host.com>'.
#
# Deprecated: Group id containing anything except ASCII digits.
# Group name containing charactersoutside the ASCII range(b'\x00' - b'\x7f') in bytes replacement strings.
# The special sequences consist of '\' ' \and a character from the list below.
# If the ordinary character is not an ASCII digit or an ASCII letter, then the resulting RE will match
# the second character. For example, \$ matches the character '$'.
#
# # \number
# Matches the contents of the group of the same number. Groups are numbered starting from 1.
# For example, (.+) \1 matches 'the the' or '55 55', but not 'thethe' (note the space after the group).
# This special sequence can only be used to match one of the first 99 groups.
# If the first digit of number is 0, or number is 3 octal digits long, it will not be
# interpreted as a group match, but as the character with octal value number.
# Inside the '[' and ']' of a character class, all numeric escapes are treated as characters.
#
# # \A
# Matches only at the start of the string.
#
# # \b
# Matches the empty string, but only at the beginning or end of a word.
# A word is defined as a sequence of word characters. Note that formally, \b is defined as the boundary between a
# \w and a \W character (or vice versa), or between \w and the# beginning / end of the string.
# This means that r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'.
#
# By default Unicode alphanumerics are the ones used in Unicode patterns,
# but this can be changed by using the ASCII flag.
# Word boundaries are determined by the current locale if the LOCALE flag is used.
# Inside a character range, \b represents the backspace character, for compatibility with Python’s string literals.
#
# # \B
# Matches the empty string, but only when it is not at the beginning or end of a word.This means that r'py\B' matches
# 'python', 'py3', 'py2', but not 'py', 'py.', or 'py!'. \B is just the opposite of \b, so word characters in Unicode
# patterns are Unicode alphanumerics or the underscore, although this can be changed by using the ASCII flag.
# Word boundaries are determined by the current locale if the LOCALE flag is used.
#
# # \d
# For Unicode(str) patterns:
# Matches any Unicode decimal digit (that is, any character in Unicode character category[Nd]).
# This includes[0 - 9], and also many other digit characters.
#
# For 8-bit(bytes) patterns или с ASCII-флагом:
# equivalent to [0-9].
#
# # \D
# Matches any character which is not a decimal digit.This is the opposite of \d.
# If the ASCII flag is used this becomes the equivalent of[^0-9].
#
# # \s
# For Unicode(str) patterns:
# Matches Unicode whitespace characters(which includes[ \t\n\r\f\v], and also many other characters,
# for example the non-breaking spaces mandated by typography rules in many languages).
# If the ASCII flag is used, only[ \t\n\r\f\v] is matched.
#
# For 8-bit(bytes) patterns:
# Matches characters considered whitespace in the ASCII character set; this is equivalent to [\t\n\r\f\v].
#
# # \S
# Matches any character which is not a whitespace character. This is the opposite of \s.
# С ASCII-флагом равно [^ \t\n\r\f\v].
#
# # \w
# For Unicode(str) patterns:
# Matches Unicode word characters; this includes alphanumeric characters (as defined by str.isalnum()) as well as the
# underscore(_).If the ASCII flag is used, only [a-zA-Z0-9_] is matched.
#
# For 8-bit(bytes) patterns:
# Matches characters considered alphanumeric in the ASCII character set; this is equivalent to [a-zA-Z0-9_].
# If the LOCALE flag is used, matches characters considered alphanumeric in the current locale and the underscore.
#
# # \W
# Matches any character which is not a word character.This is the opposite of \w.
# If the ASCII flag is used this becomes the equivalent of[^a-zA-Z0-9_].
# If the LOCALE flag is used, matches characters which are neither alphanumeric in the current locale nor '_'.
#
# # \Z
# Matches only at the end of the string.
#
# Most of the standard escapes supported by Python string literals are also accepted by the regular expression parser:
#
# \a      \b      \f      \n
# \N      \r      \t      \u
# \U      \v      \x      \\
#
# (Note that \b is used to represent word boundaries, and means “backspace” only inside character classes.)
#  '\u', '\U', and '\N' escape sequences are only recognized in Unicode patterns. In bytes patterns they are errors.
# Unknown escapes of ASCII letters are reserved for future use and treated as errors.
# Octal escapes are included in a limited form.
# If the first digit is a 0, or if there are three octal digits, it is considered an octal escape.
# Otherwise, it is a group reference. As for string literals, octal escapes are always at most three digits in length.
# Unknown escapes consisting of '\' and an ASCII letter are errors.
# The '\N{name}' escape sequence has been added.
# As in string literals, it expands to the named Unicode character (e.g.'\N{EM DASH}').

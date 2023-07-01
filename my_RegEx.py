""" Мой гайд по регулярным выражениям"""
# import re

# Мы используем в регулярных выражениях префикс 'r' (raw string) чтобы не происходило вещей типа "\\\\" для поиска
# одной косой черты ('\\\\' = '\\' в Python = '\' в обычной жизни).
# Вместо этого можно использовать r'\\' (что для Python так же будет '\\', т.е. просто '\'.
# Цитата -- "it’s highly recommended that you use raw strings for all but the simplest expressions".

########################################################################################################################
#                                                 Функции re:
########################################################################################################################

# разница между re.search("^a", "abcd") и re.match("a", "abcd"): обе команды будут искать "a" только в начале,
# но search с флагом MULTILINE может искать не только в начале Строки, но и в подстроках.

# re.compile(pattern, flags=0)
# Позволяет сохранить паттерн для многократного использования и экономии ресурсов.

# re.escape(pattern)
# Если мы используем строку в качестве паттерна, то escape делает эту строку "безопасной"
# (например, в адресе сайта экранирует точки, чтобы они искались как точки, а не как спец. символы).

# re.findall(pattern, string, flags=0)
# Возвращает список объектов или кортежей. Поиск по группам?..

# re.finditer(pattern, string, flags=0)
# Возвращает генератор, который выдаёт все совпадения.

# re.fullmatch(pattern, string, flags=0)
# Вся строка должна совпадать с паттерном.

# re.match(pattern, string, flags=0)
# Ищет только в начале Строки. MULTILINE ничего не меняет, видимо.

# re.purge()
# "Clear the regular expression cache", что бы это не значило.

# re.search(pattern, string, flags=0)
# Ищет где угодно в Строке (не только в начале). При использовании '^' схож с функцией re.match(), но при использовании
# флага MULTILINE может искать в начале не только Строки, но ещё и подстрок.

# re.split(pattern, string, maxsplit=0, flags=0)
# Возвращает список деления строки по паттерну.

# re.sub(pattern, repl, string, count=0, flags=0)
# Возвращает string, где pattern заменён на repl. Много нюансов использования!

# re.subn(pattern, repl, string, count=0, flags=0)
# То же, что и re.sub(), но возвращает кортеж (новая строка, кол-во замен).

# re.template(pattern, flags) -- непонятно.

########################################################################################################################
#                                                      Исключения
########################################################################################################################
# Можно вызвать исключение, если со строкой что-то не так.

########################################################################################################################
#                                                        Флаги
########################################################################################################################

# re.A = re.ASCII = (?a)
# По умолчанию поиск ведётся в Unicode, этот флаг делает \w, \W, \b, \B, \d, \D, \s и \S ASCII-only.

# re.DEBUG -- что-то непонятное про дебаггинг.

# re.I = re.IGNORECASE = (?i)
# Не обращает внимания на регистр букв.

# re.L = re.LOCALE = (?L)
# Флаг локалей (только для 8-битного поиска!).

# re.M = re.MULTILINE = (?m)
# С этим флагом '^' соответствует не только началу Строки, но и началу подсток (после '\n'), а '$' соответствует
# не только концу Строки, но и конце подстрок (перед '\n').

# re.NOFLAG
# Используется для создания своих функций с флагами:
# def myfunc(text, flag=re.NOFLAG):
#    return re.match(text, flag)

# re.S = re.DOTALL = (?s)
# С этим флагом точка ('.') заменяет и символ новой строки ('\n').

# re.X = re.VERBOSE = (?x)
# Даёт возможность визуально разбивать регулярные выражения и добавлять к ним комментарии.
# Пробелы в выражении (если не в [], не '\ ' и не в случаях типа '*?', '(?:' или '(?P<...>') игнорируются.
# Т.е.добавить пробел и сделать '(? :' или '* ?' не получится.
# Символы после '#' и до конца строки игнорируются (кроме случаев '\#' и внутри []).

# Ниже a и b равны:
# a = re.compile(r"""\d +  # the integral part
#                    \.    # the decimal point
#                    \d *  # some fractional digits""", re.X)
# b = re.compile(r"\d+\.\d*")

########################################################################################################################
#                                            Методы объектов Match и Pattern
########################################################################################################################

# Так как match() and search() возвращают None при отсутствии совпадений, можно проверить было ли совпадение простым if:
# my_match = re.search(pattern, string)
# if my_match:
#     process(my_match)

# Match.expand(template)  #todo
# Return the string obtained by doing backslash substitution on the template string template, as done by the sub()
# method. Escapes such as \n are converted to the appropriate characters,
# and numeric backreferences (\1, \2) and named backreferences (\g<1>, \g<name>) are replaced
# by the contents of the corresponding group.
# Unmatched groups are replaced with an empty string.

# Match.group([group1, ...])  #todo
# Returns one or more subgroups of the match. If there is a single argument, the result is a single string;
# if there are multiple arguments, the result is a tuple with one item per argument.
# Without arguments, group1 defaults to zero (the whole match is returned). If a groupN argument is zero,
# the corresponding return value is the entire matching string; if it is in the inclusive range [1..99],
# it is the string matching the corresponding parenthesized group. If a group number is negative or larger than
# the number of groups defined in the pattern, an IndexError exception is raised.
# If a group is contained in a part of the pattern that did not match, the corresponding result is None.
# If a group is contained in a part of the pattern that matched multiple times, the last match is returned.
#
# m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
# m.group(0)       # The entire match
# 'Isaac Newton'
# m.group(1)       # The first parenthesized subgroup.
# 'Isaac'
# m.group(2)       # The second parenthesized subgroup.
# 'Newton'
# m.group(1, 2)    # Multiple arguments give us a tuple.
# ('Isaac', 'Newton')
#
# If the regular expression uses the (?P<name>...) syntax, the groupN arguments may also be
# strings identifying groups by their group name. If a string argument is not used as a group name in the pattern,
# an IndexError exception is raised.
#
# A moderately complicated example:
#
# m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
# m.group('first_name')
# 'Malcolm'
# m.group('last_name')
# 'Reynolds'
#
# Named groups can also be referred to by their index:
# m.group(1)
# 'Malcolm'
# m.group(2)
# 'Reynolds'
#
# If a group matches multiple times, only the last match is accessible:
# m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times.
# m.group(1)                        # Returns only the last match.
# 'c3'

# Match.__getitem__(g)  #todo
# То же самое, что и  m.group(g) и даёт более простой доступ к инд. группе из мэтча:
#
# m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
# m[0]       # The entire match
# 'Isaac Newton'
# m[1]       # The first parenthesized subgroup.
# 'Isaac'
# m[2]       # The second parenthesized subgroup.
# 'Newton'
#
# Named groups тоже поддерживаются/ возможны:
# m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Isaac Newton")
# m['first_name']
# 'Isaac'
# m['last_name']
# 'Newton'

# Match.groups(default=None)  #todo
# Return a tuple containing all the subgroups of the match, from 1 up to however many groups are in the pattern.
# The default argument is used for groups that did not participate in the match; it defaults to None.
#
# For example:
# m = re.match(r"(\d+)\.(\d+)", "24.1632")
# m.groups()
# ('24', '1632')
#
# If we make the decimal place and everything after it optional, not all groups might participate in the match.
# These groups will default to None unless the default argument is given:
#
# m = re.match(r"(\d+)\.?(\d+)?", "24")
# m.groups()      # Second group defaults to None.
# ('24', None)
# m.groups('0')   # Now, the second group defaults to '0'.
# ('24', '0')

# Match.groupdict(default=None)  #todo
# Return a dictionary containing all the named subgroups of the match, keyed by the subgroup name.
# The default argument is used for groups that did not participate in the match; it defaults to None. For example:
#
# m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
# m.groupdict()
# {'first_name': 'Malcolm', 'last_name': 'Reynolds'}

# Match.start([group])  #todo
# Match.end([group])
# Return the indices of the start and end of the substring matched by group; group defaults to zero
# (meaning the whole matched substring). Return -1 if group exists but did not contribute to the match.
# For a match object m, and a group g that did contribute to the match, the substring matched by group g
# (equivalent to m.group(g)) is m.string[m.start(g):m.end(g)]
#
# Note that m.start(group) will equal m.end(group) if group matched a null string. For example,
# after m = re.search('b(c?)', 'cba'), m.start(0) is 1, m.end(0) is 2, m.start(1) and m.end(1) are both 2,
# and m.start(2) raises an IndexError exception.
#
# Пример того, как убрать строку 'remove_this' из email адреса:
# email = "tony@tiremove_thisger.net"
# m = re.search("remove_this", email)
# email[:m.start()] + email[m.end():]
# 'tony@tiger.net'

# Match.span([group])  #todo
# For a match m, return the 2-tuple (m.start(group), m.end(group)). Note that if group did not contribute to the match,
# this is (-1, -1). group defaults to zero, the entire match.

# Match.pos  #todo
# The value of pos which was passed to the search() or match() method of a regex object.
# This is the index into the string at which the RE engine started looking for a match.

# Match.endpos  #todo
# The value of endpos which was passed to the search() or match() method of a regex object.
# This is the index into the string beyond which the RE engine will not go.

# Match.lastindex  #todo
# The integer index of the last matched capturing group, or None if no group was matched at all.
# For example, the expressions (a)b, ((a)(b)), and ((ab)) will have lastindex == 1 if applied to the string 'ab',
# while the expression (a)(b) will have lastindex == 2, if applied to the same string.

# Match.lastgroup  #todo
# The name of the last matched capturing group, or None if the group didn’t have a name, or if no group was matched
# at all.

# Match.re  #todo
# The regular expression object whose match() or search() method produced this match instance.

# Match.string  #todo
# The string passed to match() or search().
#
# Added support of copy.copy() and copy.deepcopy(). Match objects are considered atomic.

# Pattern.search(string[, pos[, endpos]])  #todo
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

# Pattern.match(string[, pos[, endpos]])  #todo
# If zero or more characters at the beginning of string match this regular expression, return a corresponding
# match object. Return None if the string does not match the pattern; note that this is different from a
# zero-length match.
#
# The optional pos and endpos parameters have the same meaning as for the search() method.
#
# pattern = re.compile("o")
# pattern.match("dog")      # No match as "o" is not at the start of "dog".
# pattern.match("dog", 1)   # Match as "o" is the 2nd character of "dog".
# <re.Match object; span=(1, 2), match='o'>
#
# If you want to locate a match anywhere in string, use search() instead (see also search() vs. match()).

# Pattern.fullmatch(string[, pos[, endpos]])  #todo
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

# Pattern.split(string, maxsplit=0)  #todo
# Identical to the split() function, using the compiled pattern.

# Pattern.findall(string[, pos[, endpos]])  #todo
# Similar to the findall() function, using the compiled pattern, but also accepts optional pos and endpos parameters
# that limit the search region like for search().

# Pattern.finditer(string[, pos[, endpos]])  #todo
# Similar to the finditer() function, using the compiled pattern, but also accepts optional pos and endpos parameters
# that limit the search region like for search().

# Pattern.sub(repl, string, count=0)  #todo
# Identical to the sub() function, using the compiled pattern.

# Pattern.subn(repl, string, count=0)  #todo
# Identical to the subn() function, using the compiled pattern.

# Pattern.flags  #todo
# The regex matching flags. This is a combination of the flags given to compile(), any (?...) inline flags
# in the pattern, and implicit flags such as UNICODE if the pattern is a Unicode string.

# Pattern.groups  #todo
# The number of capturing groups in the pattern.

# Pattern.groupindex  #todo
# A dictionary mapping any symbolic group names defined by (?P<id>) to group numbers. The dictionary is empty
# if no symbolic groups were used in the pattern.

# Pattern.pattern  #todo
# The pattern string from which the pattern object was compiled.
# Added support of copy.copy() and copy.deepcopy(). Compiled regular expression objects are considered atomic.

########################################################################################################################
#                                            Спецсимволы и спецвыражения
########################################################################################################################

# '.'
# Любой символ (чтобы включал в себя '\n' надо использовать флаг DOTALL).

# '^'
# Начало Строки, вместе с флагом MULTILINE также начало подстрочек.

# '$'
# Без флага MULTILINE соответствует концу Строки (в т.ч. с \n), с MULTILINE соответствует ещё и
# концам подстрочек (т.е. всем \n). Выражение 'foo' соответствует как ‘foo’, так и ‘foobar’, а выражение 'foo$'
# соответствует только ‘foo’. Ещё пример: выражение 'foo.$' в строке 'foo1\nfoo2\n' без флага MULTILINE соответствует
# только ‘foo2’, но со флагом MULTILINE ещё и ‘foo1’; выражению '$' в строке 'foo\n' соответствуют два пустых рез-та:
# один прямо до \n и один в конце строки.

# '*'
# Предыдущий элемент любое количество раз. Выражение ab* значит "a и сколько угодно (0+) b".

# '+'
# Предыдущий элемент 1 или больше раз. Выражение ab+ значит "ab, где b может быть сколько угодно, главное не 0".

# '?'
# Предыдущий элемент 0 или 1 раз. Выражение 'ab?' значит "a и либо 1 либо 0 раз b", т.е. либо ‘a’ либо ‘ab’.

# '*?', '+?', '??'
# Операторы '*', '+' и '?' жадные, т.е. соответствуют как можно большему объему текста. Добавлением '?' после
# этих операторов мы излечиваем их жадность, т.е. они будут соответствовать минимальному объему текста. Например:
# - выражению <.*> соответствует вся строка '<a> b <c>'.
# - выражению <.*?> соответствует только '<a>'.

# '*+', '++', '?+'  #todo
# Like the '*', '+', and '?' quantifiers, those where '+' is appended also match as many times as possible.
# However, unlike the true greedy quantifiers, these do not allow back-tracking when the expression following it
# fails to match. For example, a * a will match 'aaaa' because the a * will
# match all 4 'a' s, but, when the final 'a' is encountered, the expression is backtracked so that in the end
# the a * ends up matching 3 'a' s total, and the fourth 'a' is matched by the final 'a'. However, when a * +a is used
# to match 'aaaa', the a * + will match all 4 'a', but when the final 'a' fails to find any more characters to match,
# the expression cannot be backtracked and will thus fail to match.
# То есть 'x*+' == '(?>x*)', 'x++' == '(?>x+)' и 'x?+' == '(?>x?)'.

# '{m}'
# Предыдущий элемент должен быть ровно m число раз. Выражение 'a{6}' значит 'aaaaaa', но не 'aaaaa'.

# '{m, n}'
# Определяет нижнюю и верхнюю границы количества символа до него.
# Например, выражению 'a{3, 5}' соответствует 'aaa', 'aaaa' и 'aaaaa'. По возможности возвращает как можно большее число
# символов (жадный).По умолчанию нижняя граница принимается за 0, верхняя за бесконечность.
# Например, выражению 'a{4, }b' соответствуют как 'aaaab' , так и 1000 букв'a' перед 'b', но не 'aaab'.

# '{m, n}?'
# То же, что и верхнее, но не жадное (довольствуется минимальным совпадением). Разница: выражение a{3,5} в строке
# 'aaaaaa' вернёт 5 'a', а выражение a{3,5}? вернёт только три 'a'.

# '{m, n}+'  #todo
# Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many
# repetitions as possible without establishing any backtracking points.This is the possessive version of the
# quantifier above.For example, on the 6 - character string 'aaaaaa', a {3, 5} + aa attempt to match 5
# 'a' characters, then, requiring 2 more 'a' s, will need more characters than available and thus fail,
# while a{3, 5}aa will match with a{3, 5} capturing 5, then 4 'a's by backtracking and then the final 2 'a's are
# matched by the final aa in the pattern.x{m, n}+ is equivalent to (? > x{m, n}).

# '\'
# Escape-символ

# '[]'
# Набор символов. В том числе:
# -Просто допустимые символы (выражению '[amk]' соответствует 'a', 'm' или 'k').
#
# -Диапазоны значений, например, [0-5][0-9] соответствует всем двузначным числам от 00 до 59.
# Чтобы дефис искался сам по себе, его надо либо экранировать ('[a\-z]') или поместить на первое ('[-a]') или последнее
# ('[a-]') место в скобках.
#
# -NB: внутри [] спец.символы становятся обычными. Например, выражению '[(+ *)]' просто значит "любой из этих символов:
#  '(', '+', '*' и ')'".
#
# -Наборы символов типа \w or \S в [] сохраняют своё значение.
#
# -Чтобы найти любой символ, кроме определённого (например пятерки), мы ставим перед ним '^' -- [^5].
# -Если сначала в [] поставить '^' это будет значить "кроме этих символов. '[^5]' значит "что угодно кроме пятерки",
# а '[^^]' -- "что угодно кроме '^'"
#
# Чтобы найти соответствие символу ']', мы должны либо его экранировать ('[()[\]{}]'), либо поставить на
# первое место ('[]()[{}]').
# Чтобы не было ошибок, надо экранировать '[', '--', '&&', '~~' и '||'.

# '|'  #todo
# A | B, where A and B can be arbitrary REs, creates a regular expression that will match either A or B.
# An arbitrary number of REs can be separated by the '|' in this way.
# Также может использоваться внутри групп.
# As the target string is scanned, REs separated by '|' are tried from left to right. When one pattern completely
# matches, that branch is accepted. This means that once A matches, B will not be tested further,
# even if it would produce a longer overall match. In other words, the '|' operator is never greedy.
# To match a literal '|', use \|, or enclose it inside [] , as in '[|]'.

# '(...)'  #todo
# Группа внутри рег. выражения.
# The contents of a group can be retrieved after a match has been performed, and can be matched later in the string with
# the \number special sequence.
# Чтобы найти просто символы '(' или ')', их надо экранировать ('\(' и '\)') или поставить в [] ('[(]' и '[)]').

#######################################################################################################################
#                                                       Extensions
########################################################################################################################

# '(?aiLmsux)'
# Можно включить флаги в само регулярное выражение (напр. для compile): (?флаг(-и)) должны стоять первыми в выражении!

# '(?:...)'  #todo
# A non-capturing version of regular parentheses. Matches whatever regular expression is inside the parentheses,
# but the substring matched by the group can't be retrieved after performing a match or referenced later in the pattern.

# '(?aiLmsux-imsx:...)'  #todo
# (Zero or more letters from the set 'a', 'i', 'L', 'm', 's', 'u', 'x', optionally followed by '-' followed by
# one or more letters from the 'i', 'm', 's', 'x'.)
# Буквы ставят или убирают флаги re.A, re.I, re.L, re.M, re.S, re.U, and re.X для части выражения.
# Так как флаги 'a', 'L' и 'u' взаимоисключающие, их нельзя комбинировать или ставить после '-'.
# Вместо этого, when one of them appears in an inline group, it overrides the matching mode in the enclosing group.
# In Unicode patterns(?a: ...) switches to ASCII - only matching, and (?u:...) switches to Unicode matching(default).
# In byte pattern(?L: ...) switches to locale depending matching,
# and (?a:...) switches to ASCII-only matching (default).
# This override is only in effect for the narrow inline group, and the original matching mode is restored outside of
# the group.

# '(?>...)'  #todo
# Attempts to match... as if it was a separate regular expression, and if successful, continues to match the rest
# of the pattern following it. If the subsequent pattern fails to match, the stack can only be unwound to a point
# before the (? >...) because once exited, the expression, known as an atomic group, has thrown away all stack points
# within itself.
# Thus, '(? >.* ).' would never match anything because first the '.*' would match all characters possible, then,
# having nothing left to match, the final '.' would fail to match.
# Since there are no stack points saved in the Atomic Group, and there is no stack point before it,
# the entire expression would thus fail to match.

# '(?P<name>...)'  #todo
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

# '(?P=name)'  #todo
# A backreference to a named group; it matches whatever text was matched by the earlier group named name.

# '(?#...)'
# Комментарий, содержимое внутри скобок игнорируется.

# '(?=...)'
# Соответствует только если после выражения идёт ... Например, Isaac(?=Asimov) соответствует 'Isaac' только если
# после него идёт 'Asimov'.

# '(?!...)'
# Соответствует, кроме тех случаев, когда сразу после выражения идёт ... . Например, Isaac(?!Asimov) соответствует
# 'Isaac' только если после него не идёт 'Asimov'.

# '(?<=...)'  #todo
# Matches if the current position in the string is preceded by a match for ... that ends at the current position.
# (? <= abc)def will find a match in 'abcdef',
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

# '(?<!...)'  #todo
# Matches if the current position in the string is not preceded by a match for ....
# Как и штука выше, the contained pattern must only match strings of some fixed length.
# Patterns which start with negative lookbehind assertions may match at the beginning of the string being searched.

# '(?(id/name)yes-pattern|no-pattern)'  #todo
# Will try to match with yes-pattern if the group with given id or name exists, and with no-pattern if it doesn’t.
# No-pattern is optional and can be omitted.
# For example, ( < )?(\w+ @ \w+(?:\.\w +)+)(?(1) > | $) is a poor email matching pattern, which will match with
# '<user@host.com>' as well as 'user@host.com', but not with '<user@host.com' nor 'user@host.com>'.

# '\number' #todo
# Matches the contents of the group of the same number. Groups are numbered starting from 1.
# For example, (.+) \1 matches 'the the' or '55 55', but not 'thethe' (note the space after the group).
# This special sequence can only be used to match one of the first 99 groups.
# Inside the '[' and ']', all numeric escapes are treated as characters.

# '\A' -- непонятно
# Matches only at the start of the string.

# '\b'
# Соответствует пустой строке, но только в начале или конце слова.
# (Слово -- последовательность \w). Формально, \b это граница между '\w' и либо '\W', либо началом/ концом строки.
# Например, r'\bfoo\b' соответствует 'foo', 'foo.', '(foo)', 'bar foo baz' но не 'foobar' или 'foo3'.
# При использовании LOCALE-флага границы слов определяются локалью.
# Inside a character range, \b represents the backspace character, for compatibility with Python’s string literals.

# '\B'
# «Антоним» '\b'. "Соответствует пустой строке, но только когда она не в начале или в конце слова".
# Например, r'py\B' соответствует 'python', 'py3', 'py2', но не 'py', 'py.' или 'py!'.
# При использовании LOCALE-флага границы слов определяются локалью.

# '\d'
# В Unicode: любая цифра (обычные '[0-9]' и ещё много других). Для 8-bit или с ASCII-флагом равно '[0-9]'.

# '\D'
# «Антоним» '\d'. Соответствует любому символу не цифре. С ASCII-флагом равно '[^0-9]'.

# '\s'
# В Unicode: '[ \t\n\r\f\v]' и множество других символов, например неразрывные пробелы.
# Для 8-bit или с ASCII-флагом равно '[ \t\n\r\f\v]'.

# '\S'
# «Антоним» '\s', включая неразрывные пробелы и т.п. С ASCII-флагом равно '[^ \t\n\r\f\v]'.

# '\w'
# В Unicode: '_' и всё, что считается буквой/цифрой в Unicode. С ASCII-флагом только '[a-zA-Z0-9_]'.
# Для 8-bit: как и ASCII равно [a-zA-Z0-9_]. С LOCALE-флагом соответствует '_' и цифрам/буквам локали.

# '\W'
# «Антоним» '\w', всё, что не считается буквой/ цифрой в Unicode.
# С ASCII-флагом равно '[^a-zA-Z0-9_]'.
# С LOCALE-флагом всё кроме '_' и цифр/букв локали.

# '\Z' -- непонятно
# Matches only at the end of the string.

# Escape-последовательности Python и регулярных выражений совпадают (за исключением '\b').

from text_analysis import TextStats

text = input("Введіть текст для аналізу:\n")

analyzer = TextStats(text)

print("\n=== Статистика тексту ===")
print("Кількість слів:", analyzer.count_words())

most_common = analyzer.most_common_letter()
if most_common:
    print(f"Найчастіша літера: '{most_common[0]}' (зустрічається {most_common[1]} разів)")
else:
    print("У тексті немає літер.")

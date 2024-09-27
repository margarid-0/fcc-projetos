import pandas as pd

df = pd.read_csv('adult.data.csv', header=None)

# Nomear as colunas 
df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 
              'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
              'hours-per-week', 'native-country', 'salary']

def calculate_demographic_data(print_data=True):
    # Cálculo quantidade de raças
    race_count = df['race'].value_counts()

    # Idade média dos homens
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Porcentagem de bacharelado
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Porcentagem de pessoas com bacharelado, mestrado ou doutorado.
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # Porcentagem de salário > 50K.
    higher_education_rich = round((df[higher_education & (df['salary'] == '>50K')].shape[0] / df[higher_education].shape[0]) * 100, 1)
    lower_education_rich = round((df[lower_education & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0]) * 100, 1)

    # Minímo de horas trabalhadas por uma pessoa.
    min_work_hours = df['hours-per-week'].min()

    # Porcentagem de pessoas que trabalham o número mínimo de horas e tem salário > 50K.
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # Qual país tem a maior porcentagem de pessoas ganhando > 50K?
    country_salary = df[df['salary'] == '>50K'].groupby('native-country').size()
    country_total = df.groupby('native-country').size()
    highest_earning_country_percentage = round((country_salary / country_total * 100).max(), 1)
    highest_earning_country = (country_salary / country_total * 100).idxmax()

    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0] if not df[(df['native-country'] == 'India') & (df['salary'] == '>50K')].empty else None

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()
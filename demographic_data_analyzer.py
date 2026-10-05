import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    col_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
        'salary'
    ]
    df = pd.read_csv('adult.data', names=col_names, skipinitialspace=True)

    # Q1. How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # Q2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Q3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').mean() * 100, 1
    )

    # Q4 & Q5. Advanced vs non-advanced education >50K earners
    advanced_education = df['education'].isin(
        ['Bachelors', 'Masters', 'Doctorate']
    )

    higher_education = df[advanced_education]
    lower_education = df[~advanced_education]

    higher_education_rich = round(
        (higher_education['salary'] == '>50K').mean() * 100, 1
    )
    lower_education_rich = round(
        (lower_education['salary'] == '>50K').mean() * 100, 1
    )

    # Q6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # Q7. Percentage of min-hour workers earning >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # Q8. Country with highest % of >50K earners
    country_stats = (
        df.groupby('native-country')['salary']
          .apply(lambda s: (s == '>50K').mean() * 100)
    )
    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(), 1)

    # Q9. Most popular occupation for >50K earners in India
    top_IN_occupation = (
        df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
          ['occupation']
          .value_counts()
          .idxmax()
    )

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: "
            f"{higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: "
            f"{lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: "
            f"{rich_percentage}%"
        )
        print(
            "Country with highest percentage of rich:",
            highest_earning_country
        )
        print(
            "Highest percentage of rich people in country:",
            highest_earning_country_percentage
        )
        print("Top occupations in India:", top_IN_occupation)

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
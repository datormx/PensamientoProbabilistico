def calc_bayes(prior_A, prob_B_dado_A, prob_B):
    return (prior_A * prob_B_dado_A) / prob_B


if __name__ == "__main__":
    prob_cancer = 1 / 100000 #P(A)
    prob_sintoma_dado_cancer = 1 / 1 #P(B|A)
    prob_sintoma_dado_no_cancer = 10 / 99999 #P(B|¬A))
    prob_no_cancer = 1 - prob_cancer #P(¬A)

    prob_sintoma = (prob_cancer * prob_sintoma_dado_cancer) + (prob_no_cancer * prob_sintoma_dado_no_cancer) #P(B)
    print(prob_sintoma)

    prob_cancer_dado_sintoma = calc_bayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma) #P(A|B)

    print(prob_cancer_dado_sintoma)
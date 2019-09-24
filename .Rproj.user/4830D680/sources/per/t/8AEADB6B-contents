# data preprocessing


# importing the datasets
dataset <- read.csv("data-preprocessing/Data.csv")
# taking care of missing data
age <- dataset$Age <- ifelse(is.na(dataset$Age),
                             ave(
                               dataset$Age,
                               FUN = function(x)
                                 mean(x, na.rm = TRUE)
                             ),
                             dataset$Age)
View(age)
dataset

salary <- dataset$Salary <- ifelse(is.na(dataset$Salary),
                             ave(
                               dataset$Salary,
                               FUN = function(x)
                                 mean(x, na.rm = TRUE)
                             ),
                             dataset$Salary)

dataset

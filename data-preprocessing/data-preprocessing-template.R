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

# # Encoding categorical data
dataset$Country = factor(
  dataset$Country,
  levels = c('France', 'Germany', 'Spain'),
  labels = c(1, 2, 3)
)

dataset

dataset$Purchased = factor(dataset$Purchased,
                           levels = c("No", 'Yes'),
                           labels = c(0, 1))

dataset

# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)

training_set = subset(dataset, split == TRUE)
test_Set = subset(dataset, split == FALSE)


# feature scaling
training_set[, 2:3] = scale(training_set[, 2:3])
test_Set[, 2:3] = scale(test_Set[, 2:3])

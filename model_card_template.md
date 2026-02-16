# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This machine learning (ML) model utilizes a classification model (RandomForestClassifier) on the dataset. Using different packages from the scikit-learn 1.5.1 library, such as LabelBinarizer, OneHotEncoder, and RandomForestClassifier, it performs data slicing on various aspects of a dataset with categorical data.

## Intended Use
This ML model performs data slicing on U.S. Census data from 1994. The dataset has different categories, each with categorical data features (workclass, sex, and age, for example), and the model slices that data to form predictions to determine if certain recorded characteristics can predict one's salary. An intended user for this model would be employees (prospective or current) looking to determine what their true salary should be given their backgrounds.

## Training Data
This ML model uses public data collected in 1994 from the most recent U.S. Census at the time. It was published by the University of California, Irvine's Machine Learning Repository (Source: https://archive.ics.uci.edu/dataset/20/census+income). 

The dataset recorded different employment and demographic data categories of the recorded subjects, including (but not limited to) private or self employment, education level, sex, and salary (below or above fifty thousand dollars).  

## Evaluation Data
Training and testing datasets were created from the larger Census data set. The dataset was divided on an 80/20 split. Eighty percent of the data was in the "train" dataset and twenty percent in the "test" dataset.

## Metrics
_Please include the metrics used and your model's performance on those metrics._

The metrics that were used in evaluating the ML model's performance were Precision, Recall, and F1. The Precision value was 0.7260, the value for Recall was 0.6484, and the F1 score was 0.6850. 

## Ethical Considerations

As mentioned previously, this model uses U.S. Census data with demographic data. Demographic data is used to inform an individual's salary and employment. While elements of one's background, such as education level and hours per week can determine how much they get paid for their work, they along with race and sex, can also inform the same thing as well as whether they get hired in the first place. 

## Caveats and Recommendations

For more accurate conclusions, testing on a more expansive dataset is recommended.
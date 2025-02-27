#Task 2.1_R
# Download dataset
url <- "https://raw.githubusercontent.com/HackBio-Internship/2025_project_collection/refs/heads/main/Python/Dataset/mcgc.tsv"
#Read dataset
OD600 <- read.delim(url, header = TRUE)
#check structure and dimensions of the dataset
str(OD600)
dim(OD600)
head(OD600)

#Check If Any Missing Values Exist
any(is.na(OD600))

#Find mean OD600 Values for each strain technical replicates into new columns
OD600$S1R1WT <- rowMeans(OD600[, c("A1", "B1", "C1")], na.rm = TRUE) # Select the columns specific to Strain1Rep1 Wild Type
OD600$S1R1MT <- rowMeans(OD600[, c("A2", "B2", "C2")], na.rm = TRUE) # Select the columns specific to Strain1Rep1 Mutant Type
OD600$S1R2WT <- rowMeans(OD600[, c("A3", "B3", "C3")], na.rm = TRUE) # Select the columns specific to Strain1Rep2 Wild Type
OD600$S1R2MT <- rowMeans(OD600[, c("A4", "B4", "C4")], na.rm = TRUE) # Select the columns specific to Strain1Rep2 Mutant Type
OD600$S2R1WT <- rowMeans(OD600[, c("A5", "B5", "C5")], na.rm = TRUE) # Select the columns specific to Strain2Rep1 Wild Type
OD600$S2R1MT <- rowMeans(OD600[, c("A6", "B6", "C6")], na.rm = TRUE) # Select the columns specific to Strain2Rep1 Mutant Type
OD600$S2R2WT <- rowMeans(OD600[, c("A7", "B7", "C7")], na.rm = TRUE) # Select the columns specific to Strain2Rep2 Wild Type
OD600$S2R2MT <- rowMeans(OD600[, c("A8", "B8", "C8")], na.rm = TRUE) # Select the columns specific to Strain2Rep2 Mutant Type
OD600$S3R1WT <- rowMeans(OD600[, c("A9", "B9", "C9")], na.rm = TRUE) # Select the columns specific to Strain3Rep1 wild Type
OD600$S3R1MT <- rowMeans(OD600[, c("A10", "B10", "C10")], na.rm = TRUE) # Select the columns specific to Strain3Rep1 Mutant Type
OD600$S3R2WT <- rowMeans(OD600[, c("A11", "B11", "C11")], na.rm = TRUE) # Select the columns specific to Strain3Rep2 wild Type
OD600$S3R2MT <- rowMeans(OD600[, c("A12", "B12", "C12")], na.rm = TRUE) # Select the columns specific to Strain3Rep2 Mutant Type

#Plot OD600 vs time
library(ggplot2)

#Strain1Rep1
Strain1Rep1 <- data.frame(x = OD600$time, y1 = OD600$S1R1MT, y2 = OD600$S1R1WT)

# Create the plot
ggplot(Strain1Rep1, aes(x = x)) +  # x is already defined
  geom_line(aes(y = y1, color = "Knock out/Mutant")) +
  geom_line(aes(y = y2, color = "Knock in/Wild Type")) +
  scale_color_manual(values = c("Knock out/Mutant" = "blue", "Knock in/Wild Type" = "red")) +
  labs(title = "OD600 vs. Time (Strain 1 Rep 1)", x = "Time", y = "OD600") + # More specific labels
  theme_bw()

#Strain1Rep2
Strain1Rep2 <- data.frame(x = OD600$time, y1 = OD600$S1R2MT, y2 = OD600$S1R2WT)

# Create the plot
ggplot(Strain1Rep2, aes(x = x)) +  # x is already defined
  geom_line(aes(y = y1, color = "Knock out/Mutant")) +
  geom_line(aes(y = y2, color = "Knock in/Wild Type")) +
  scale_color_manual(values = c("Knock out/Mutant" = "blue", "Knock in/Wild Type" = "red")) +
  labs(title = "OD600 vs. Time (Strain 1 Rep 2)", x = "Time", y = "OD600") + # More specific labels
  theme_bw()

#Strain2Rep1
Strain2Rep1 <- data.frame(x = OD600$time, y1 = OD600$S2R1MT, y2 = OD600$S2R1WT)

# Create the plot
ggplot(Strain2Rep1, aes(x = x)) +  # x is already defined
  geom_line(aes(y = y1, color = "Knock out/Mutant")) +
  geom_line(aes(y = y2, color = "Knock in/Wild Type")) +
  scale_color_manual(values = c("Knock out/Mutant" = "blue", "Knock in/Wild Type" = "red")) +
  labs(title = "OD600 vs. Time (Strain 2 Rep 1)", x = "Time", y = "OD600") + # More specific labels
  theme_bw()

#Strain2Rep2
Strain2Rep2 <- data.frame(x = OD600$time, y1 = OD600$S2R2MT, y2 = OD600$S2R2WT)

# Create the plot
ggplot(Strain2Rep2, aes(x = x)) +  # x is already defined
  geom_line(aes(y = y1, color = "Knock out/Mutant")) +
  geom_line(aes(y = y2, color = "Knock in/Wild Type")) +
  scale_color_manual(values = c("Knock out/Mutant" = "blue", "Knock in/Wild Type" = "red")) +
  labs(title = "OD600 vs. Time (Strain 2 Rep 2)", x = "Time", y = "OD600") + # More specific labels
  theme_bw()

#Strain3Rep1
Strain3Rep1 <- data.frame(x = OD600$time, y1 = OD600$S3R1MT, y2 = OD600$S3R1WT)

# Create the plot
ggplot(Strain3Rep1, aes(x = x)) +  # x is already defined
  geom_line(aes(y = y1, color = "Knock out/Mutant")) +
  geom_line(aes(y = y2, color = "Knock in/Wild Type")) +
  scale_color_manual(values = c("Knock out/Mutant" = "blue", "Knock in/Wild Type" = "red")) +
  labs(title = "OD600 vs. Time (Strain 3 Rep 1)", x = "Time", y = "OD600") + # More specific labels
  theme_bw()

#Strain3Rep2
Strain3Rep2 <- data.frame(x = OD600$time, y1 = OD600$S3R2MT, y2 = OD600$S3R2WT)

# Create the plot
ggplot(Strain3Rep2, aes(x = x)) +  # x is already defined
  geom_line(aes(y = y1, color = "Knock out/Mutant")) +
  geom_line(aes(y = y2, color = "Knock in/Wild Type")) +
  scale_color_manual(values = c("Knock out/Mutant" = "blue", "Knock in/Wild Type" = "red")) +
  labs(title = "OD600 vs. Time (Strain 3 Rep 2)", x = "Time", y = "OD600") + # More specific labels
  theme_bw()

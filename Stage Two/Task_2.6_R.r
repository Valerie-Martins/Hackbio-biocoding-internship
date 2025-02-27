#Task2.6_R
# Load necessary libraries
library(ggplot2)
library(dplyr)

# import dataset from file, task_26.txt

task_26

#read data
data <- task_26
colnames(data)
summary (data)

# Volcano Plot
data$Significant <- ifelse(data$pvalue < 0.01 & abs(data$log2FoldChange) > 1, "Significant", "Not Significant")

ggplot(data, aes(x=log2FoldChange, y=-log10(pvalue), color=Significant)) +
  geom_point(alpha=0.5) +
  scale_color_manual(values = c("red", "black")) +
  theme_minimal() +
  labs(title="Volcano Plot", x="Log2 Fold Change", y="-Log10(p-value)")

# Identify upregulated genes
upregulated_genes <- data %>%
  filter(log2FoldChange > 1 & pvalue < 0.01) %>%
  arrange(pvalue) %>%
  head(5)

# Identify downregulated genes
downregulated_genes <- data %>%
  filter(log2FoldChange < -1 & pvalue < 0.01) %>%
  arrange(pvalue) %>%
  head(5)

# Print results
print("Top 5 Upregulated Genes:")
print(upregulated_genes)

print("Top 5 Downregulated Genes:")
print(downregulated_genes)

hamming_distance <- function(string1, string2) {
  # Check if strings are of equal length
  if (nchar(string1) != nchar(string2)) {
    stop("strings must be of equal length")
  }
  # Convert strings to character vectors
  string1_chars <- strsplit(string1, "")[[1]]
  string2_chars <- strsplit(string2, "")[[1]]
  # Compare both vectors
  string1_chars != string2_chars
  # Count positions where characters differ
  distance <- sum(string1_chars != string2_chars)
  return(distance)
}

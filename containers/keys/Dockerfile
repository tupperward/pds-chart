# Stage 1: Build the Python script
FROM python:3.8-slim as builder

WORKDIR /app
COPY keygen.py .

# Stage 2: Final minimal image
FROM alpine:latest

# Install OpenSSL
RUN apk --no-cache add openssl

# Copy the Python script from the builder stage
COPY --from=builder /app/keygen.py /app/keygen.py

# Make the script executable
RUN chmod +x /app/keygen.py

# Set the working directory
WORKDIR /app



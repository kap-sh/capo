"""Error codes and HTTP statuses that are retried whether or not the model marks them @retryable."""

# Transient: retried with the normal backoff.
KNOWN_RETRYABLE_STATUSES = frozenset({500, 502, 503, 504})
KNOWN_RETRYABLE_CODES = frozenset(
    {"PriorRequestNotComplete", "RequestTimeout", "RequestTimeoutException"}
)

# Throttling: retried with the longer throttling backoff.
KNOWN_THROTTLING_STATUSES = frozenset({429})
KNOWN_THROTTLING_CODES = frozenset(
    {
        "BandwidthLimitExceeded",
        "EC2ThrottledException",
        "LimitExceededException",
        "PriorRequestNotComplete",
        "ProvisionedThroughputExceededException",
        "RequestLimitExceeded",
        "RequestThrottled",
        "RequestThrottledException",
        "SlowDown",
        "ThrottledException",
        "Throttling",
        "ThrottlingException",
        "TooManyRequestsException",
        "TransactionInProgressException",
    }
)

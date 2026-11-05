from __future__ import annotations

from ._base import (
    DeserializationError as DeserializationError,
)
from ._base import (
    PollyError as PollyError,
)
from ._base import (
    SerializationError as SerializationError,
)
from ._base import (
    ServiceError as ServiceError,
)
from ._base import (
    UnknownServiceError as UnknownServiceError,
)
from ._base import (
    WaiterFailedError as WaiterFailedError,
)
from ._base import (
    WaiterTimeoutError as WaiterTimeoutError,
)
from .engine_not_supported_exception import (
    EngineNotSupportedException as EngineNotSupportedException,
)
from .invalid_lexicon_exception import (
    InvalidLexiconException as InvalidLexiconException,
)
from .invalid_next_token_exception import (
    InvalidNextTokenException as InvalidNextTokenException,
)
from .invalid_s3_bucket_exception import (
    InvalidS3BucketException as InvalidS3BucketException,
)
from .invalid_s3_key_exception import InvalidS3KeyException as InvalidS3KeyException
from .invalid_sample_rate_exception import (
    InvalidSampleRateException as InvalidSampleRateException,
)
from .invalid_sns_topic_arn_exception import (
    InvalidSnsTopicArnException as InvalidSnsTopicArnException,
)
from .invalid_ssml_exception import InvalidSsmlException as InvalidSsmlException
from .invalid_tag_parameter_exception import (
    InvalidTagParameterException as InvalidTagParameterException,
)
from .invalid_task_id_exception import InvalidTaskIdException as InvalidTaskIdException
from .language_not_supported_exception import (
    LanguageNotSupportedException as LanguageNotSupportedException,
)
from .lexicon_not_found_exception import (
    LexiconNotFoundException as LexiconNotFoundException,
)
from .lexicon_size_exceeded_exception import (
    LexiconSizeExceededException as LexiconSizeExceededException,
)
from .marks_not_supported_for_format_exception import (
    MarksNotSupportedForFormatException as MarksNotSupportedForFormatException,
)
from .max_lexeme_length_exceeded_exception import (
    MaxLexemeLengthExceededException as MaxLexemeLengthExceededException,
)
from .max_lexicons_number_exceeded_exception import (
    MaxLexiconsNumberExceededException as MaxLexiconsNumberExceededException,
)
from .resource_not_found_exception import (
    ResourceNotFoundException as ResourceNotFoundException,
)
from .service_failure_exception import (
    ServiceFailureException as ServiceFailureException,
)
from .service_quota_exceeded_exception import (
    ServiceQuotaExceededException as ServiceQuotaExceededException,
)
from .ssml_marks_not_supported_for_text_type_exception import (
    SsmlMarksNotSupportedForTextTypeException as SsmlMarksNotSupportedForTextTypeException,
)
from .synthesis_task_not_found_exception import (
    SynthesisTaskNotFoundException as SynthesisTaskNotFoundException,
)
from .text_length_exceeded_exception import (
    TextLengthExceededException as TextLengthExceededException,
)
from .throttling_exception import ThrottlingException as ThrottlingException
from .too_many_tags_exception import TooManyTagsException as TooManyTagsException
from .unsupported_pls_alphabet_exception import (
    UnsupportedPlsAlphabetException as UnsupportedPlsAlphabetException,
)
from .unsupported_pls_language_exception import (
    UnsupportedPlsLanguageException as UnsupportedPlsLanguageException,
)
from .validation_exception import ValidationException as ValidationException

"""Generated from Smithy shape ``com.amazonaws.wafv2#WAFFeatureNotIncludedInPricingPlanException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import ServiceError

if TYPE_CHECKING:
    import capo_wafv2.types.disallowed_features
    import capo_wafv2.types.error_message


class WAFFeatureNotIncludedInPricingPlanException_(TypedDict, closed=True):
    message: NotRequired["capo_wafv2.types.error_message.ErrorMessage"]
    disallowed_features: NotRequired[
        "capo_wafv2.types.disallowed_features.DisallowedFeatures"
    ]
    """<p>The names of the disallowed WAF features.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFFeatureNotIncludedInPricingPlanException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "disallowed_features" in value:
        import capo_wafv2.types.disallowed_features

        out["DisallowedFeatures"] = (
            capo_wafv2.types.disallowed_features.serialize_aws_json_1_1(
                value["disallowed_features"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> WAFFeatureNotIncludedInPricingPlanException_:
    out: WAFFeatureNotIncludedInPricingPlanException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("DisallowedFeatures") is not None:
        import capo_wafv2.types.disallowed_features

        out["disallowed_features"] = (
            capo_wafv2.types.disallowed_features.deserialize_aws_json_1_1(
                data["DisallowedFeatures"]
            )
        )
    return out


class WAFFeatureNotIncludedInPricingPlanException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafv2#WAFFeatureNotIncludedInPricingPlanException``."""

    code: str | None = "WAFFeatureNotIncludedInPricingPlanException"

    def __init__(
        self,
        data: WAFFeatureNotIncludedInPricingPlanException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFFeatureNotIncludedInPricingPlanException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "WAFFeatureNotIncludedInPricingPlanException":
        return cls(deserialize_aws_json_1_1(data), message, response=response)

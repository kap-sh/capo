"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeWebAppCustomizationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.described_web_app_customization


class DescribeWebAppCustomizationResponse(TypedDict, closed=True):
    web_app_customization: "capo_transfer.types.described_web_app_customization.DescribedWebAppCustomization"
    """<p>Returns a structure that contains the details of the web app customizations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWebAppCustomizationResponse) -> dict:
    out: dict = {}
    import capo_transfer.types.described_web_app_customization

    out["WebAppCustomization"] = (
        capo_transfer.types.described_web_app_customization.serialize_aws_json_1_1(
            value["web_app_customization"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWebAppCustomizationResponse:
    out: DescribeWebAppCustomizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("WebAppCustomization") is not None:
        import capo_transfer.types.described_web_app_customization

        out["web_app_customization"] = (
            capo_transfer.types.described_web_app_customization.deserialize_aws_json_1_1(
                data["WebAppCustomization"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeWebAppCustomizationResponse.web_app_customization required"
        )
    return out


def redact_sensitive(value: DescribeWebAppCustomizationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "web_app_customization" in value:
        import capo_transfer.types.described_web_app_customization

        out["web_app_customization"] = (
            capo_transfer.types.described_web_app_customization.redact_sensitive(
                value["web_app_customization"]
            )
        )
    return out

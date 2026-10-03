"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#GetTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.template_arn


class GetTemplateRequest(TypedDict, closed=True):
    template_arn: "capo_pca_connector_ad.types.template_arn.TemplateArn"
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html">CreateTemplate</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTemplateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTemplateRequest:
    out: GetTemplateRequest = {}  # type: ignore[typeddict-item]
    return out

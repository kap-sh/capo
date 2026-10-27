"""Generated from Smithy shape ``com.amazonaws.deadline#CreateFarmRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.client_token
    import capo_deadline.types.cost_scale_factor
    import capo_deadline.types.description
    import capo_deadline.types.kms_key_arn
    import capo_deadline.types.resource_name
    import capo_deadline.types.tags


class CreateFarmRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """The unique token which the server uses to recognize retries of the same request."""
    display_name: "capo_deadline.types.resource_name.ResourceName"
    """<p>The display name of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    description: NotRequired["capo_deadline.types.description.Description"]
    """<p>The description of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    kms_key_arn: NotRequired["capo_deadline.types.kms_key_arn.KmsKeyArn"]
    """The ARN of the KMS key to use on the farm."""
    cost_scale_factor: NotRequired[
        "capo_deadline.types.cost_scale_factor.CostScaleFactor"
    ]
    """A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment. The default value is 1."""
    tags: NotRequired["capo_deadline.types.tags.Tags"]
    """The tags to add to your farm. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFarmRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "cost_scale_factor" in value:
        out["costScaleFactor"] = (
            "NaN"
            if value["cost_scale_factor"] != value["cost_scale_factor"]
            else "Infinity"
            if value["cost_scale_factor"] == float("inf")
            else "-Infinity"
            if value["cost_scale_factor"] == float("-inf")
            else value["cost_scale_factor"]
        )
    if "tags" in value:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateFarmRequest:
    out: CreateFarmRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("costScaleFactor") is not None:
        out["cost_scale_factor"] = float(data["costScaleFactor"])
    if data.get("tags") is not None:
        import capo_deadline.types.tags

        out["tags"] = capo_deadline.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateFarmRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out

"""Generated from Smithy shape ``com.amazonaws.connect#StartContactEvaluationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.auto_evaluation_configuration
    import capo_connect.types.client_token
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id
    import capo_connect.types.resource_id
    import capo_connect.types.tag_map


class StartContactEvaluationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    evaluation_form_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    auto_evaluation_configuration: NotRequired[
        "capo_connect.types.auto_evaluation_configuration.AutoEvaluationConfiguration"
    ]
    """<p>Whether automated evaluations are enabled.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartContactEvaluationRequest) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    out["EvaluationFormId"] = value["evaluation_form_id"]
    if "auto_evaluation_configuration" in value:
        import capo_connect.types.auto_evaluation_configuration

        out["AutoEvaluationConfiguration"] = (
            capo_connect.types.auto_evaluation_configuration.serialize_json(
                value["auto_evaluation_configuration"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartContactEvaluationRequest:
    out: StartContactEvaluationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("StartContactEvaluationRequest.contact_id required")
    if data.get("EvaluationFormId") is not None:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        raise DeserializationError(
            "StartContactEvaluationRequest.evaluation_form_id required"
        )
    if data.get("AutoEvaluationConfiguration") is not None:
        import capo_connect.types.auto_evaluation_configuration

        out["auto_evaluation_configuration"] = (
            capo_connect.types.auto_evaluation_configuration.deserialize_json(
                data["AutoEvaluationConfiguration"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out

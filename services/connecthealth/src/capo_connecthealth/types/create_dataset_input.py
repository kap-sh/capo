"""Generated from Smithy shape ``com.amazonaws.connecthealth#CreateDatasetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.bounded_safe_string
    import capo_connecthealth.types.dataset_config
    import capo_connecthealth.types.domain_id


class CreateDatasetInput(TypedDict, closed=True):
    domain_id: "capo_connecthealth.types.domain_id.DomainId"
    """<p>The unique identifier of the parent Domain.</p>"""
    name: "capo_connecthealth.types.bounded_safe_string.BoundedSafeString"
    """<p>A name for the dataset.</p>"""
    config: "capo_connecthealth.types.dataset_config.DatasetConfig"
    """<p>The configuration of the dataset. The member that you set determines the dataset type. You can't change the configuration after you create the dataset.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the operation returns the dataset that the first request created. If you reuse a clientToken with different parameters, the request fails with ConflictException. Use a new clientToken for a request with different parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_connecthealth.types.dataset_config

    out["config"] = capo_connecthealth.types.dataset_config.serialize_json(
        value["config"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateDatasetInput:
    out: CreateDatasetInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("config") is not None:
        import capo_connecthealth.types.dataset_config

        out["config"] = capo_connecthealth.types.dataset_config.deserialize_json(
            data["config"]
        )
    else:
        out["config"] = {"$unknown": {"name": ""}}
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out

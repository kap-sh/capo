"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#MicrovmItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_lambda_microvms.types.microvm_identifier
    import capo_lambda_microvms.types.microvm_image_arn
    import capo_lambda_microvms.types.microvm_state
    import capo_lambda_microvms.types.version


class MicrovmItem(TypedDict, closed=True):
    microvm_id: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier"
    """<p>The unique identifier of the MicroVM.</p>"""
    state: "capo_lambda_microvms.types.microvm_state.MicrovmState"
    """<p>The current lifecycle state of the MicroVM.</p>"""
    image_arn: "capo_lambda_microvms.types.microvm_image_arn.MicrovmImageArn"
    """<p>The ARN of the MicroVM image used to run this MicroVM.</p>"""
    image_version: "capo_lambda_microvms.types.version.Version"
    """<p>The version of the MicroVM image used to run this MicroVM.</p>"""
    started_at: "datetime.datetime"
    """<p>The timestamp when the MicroVM started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MicrovmItem) -> dict:
    out: dict = {}
    out["microvmId"] = value["microvm_id"]
    import capo_lambda_microvms.types.microvm_state

    out["state"] = capo_lambda_microvms.types.microvm_state.serialize_json(
        value["state"]
    )
    out["imageArn"] = value["image_arn"]
    out["imageVersion"] = value["image_version"]
    import capo_lambda_microvms.types._prelude.timestamp

    out["startedAt"] = capo_lambda_microvms.types._prelude.timestamp.serialize_json(
        value["started_at"]
    )
    return out


def deserialize_json(data: dict) -> MicrovmItem:
    out: MicrovmItem = {}  # type: ignore[typeddict-item]
    if data.get("microvmId") is not None:
        out["microvm_id"] = data["microvmId"]
    else:
        raise DeserializationError("MicrovmItem.microvm_id required")
    if data.get("state") is not None:
        import capo_lambda_microvms.types.microvm_state

        out["state"] = capo_lambda_microvms.types.microvm_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("MicrovmItem.state required")
    if data.get("imageArn") is not None:
        out["image_arn"] = data["imageArn"]
    else:
        raise DeserializationError("MicrovmItem.image_arn required")
    if data.get("imageVersion") is not None:
        out["image_version"] = data["imageVersion"]
    else:
        raise DeserializationError("MicrovmItem.image_version required")
    if data.get("startedAt") is not None:
        import capo_lambda_microvms.types._prelude.timestamp

        out["started_at"] = (
            capo_lambda_microvms.types._prelude.timestamp.deserialize_json(
                data["startedAt"]
            )
        )
    else:
        raise DeserializationError("MicrovmItem.started_at required")
    return out

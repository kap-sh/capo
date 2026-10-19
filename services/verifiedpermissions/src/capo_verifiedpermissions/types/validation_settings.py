"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ValidationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.validation_mode


class ValidationSettings(TypedDict, closed=True):
    mode: "capo_verifiedpermissions.types.validation_mode.ValidationMode"
    """<p>The validation mode currently configured for this policy store. The valid values are:</p> <ul> <li> <p> <b>OFF</b> – Neither Verified Permissions nor Cedar perform any validation on policies. No validation errors are reported by either service.</p> </li> <li> <p> <b>STRICT</b> – Requires a schema to be present in the policy store. Cedar performs validation on all submitted new or updated static policies and policy templates. Any that fail validation are rejected and Cedar doesn't store them in the policy store.</p> </li> </ul> <important> <p>If <code>Mode=STRICT</code> and the policy store doesn't contain a schema, Verified Permissions rejects all static policies and policy templates because there is no schema to validate against. </p> <p>To submit a static policy or policy template without a schema, you must turn off validation.</p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidationSettings) -> dict:
    out: dict = {}
    import capo_verifiedpermissions.types.validation_mode

    out["mode"] = capo_verifiedpermissions.types.validation_mode.serialize_aws_json_1_0(
        value["mode"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidationSettings:
    out: ValidationSettings = {}  # type: ignore[typeddict-item]
    if data.get("mode") is not None:
        import capo_verifiedpermissions.types.validation_mode

        out["mode"] = (
            capo_verifiedpermissions.types.validation_mode.deserialize_aws_json_1_0(
                data["mode"]
            )
        )
    else:
        import typing

        out["mode"] = typing.cast(
            "capo_verifiedpermissions.types.validation_mode.ValidationMode", ""
        )
    return out

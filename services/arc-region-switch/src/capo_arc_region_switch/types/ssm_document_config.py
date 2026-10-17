"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#SsmDocumentConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_region_switch.types.iam_role_arn
    import capo_arc_region_switch.types.ssm_document_arn
    import capo_arc_region_switch.types.ssm_document_parameters
    import capo_arc_region_switch.types.ssm_document_version
    import capo_arc_region_switch.types.ssm_target_list


class SsmDocumentConfig(TypedDict, closed=True):
    cross_account_role: NotRequired[
        "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross-account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    document_arn: "capo_arc_region_switch.types.ssm_document_arn.SsmDocumentArn"
    """<p>The Amazon Resource Name (ARN) of the Systems Manager document to run.</p>"""
    targets: "capo_arc_region_switch.types.ssm_target_list.SsmTargetList"
    """<p>The target filters that Systems Manager resolves to managed nodes when the command runs. To target specific managed nodes, use the <code>InstanceIds</code> key. You can specify up to five target filters.</p>"""
    parameters: NotRequired[
        "capo_arc_region_switch.types.ssm_document_parameters.SsmDocumentParameters"
    ]
    """<p>The parameters that are passed to this Region's Systems Manager document. You set parameters for each document, so each Region can run its document with its own parameters.</p>"""
    document_version: NotRequired[
        "capo_arc_region_switch.types.ssm_document_version.SsmDocumentVersion"
    ]
    """<p>The version of the Systems Manager document to run for this Region. When you omit it, Systems Manager runs the document's default version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SsmDocumentConfig) -> dict:
    out: dict = {}
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["documentArn"] = value["document_arn"]
    import capo_arc_region_switch.types.ssm_target_list

    out["targets"] = (
        capo_arc_region_switch.types.ssm_target_list.serialize_aws_json_1_0(
            value["targets"]
        )
    )
    if "parameters" in value:
        import capo_arc_region_switch.types.ssm_document_parameters

        out["parameters"] = (
            capo_arc_region_switch.types.ssm_document_parameters.serialize_aws_json_1_0(
                value["parameters"]
            )
        )
    if "document_version" in value:
        out["documentVersion"] = value["document_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SsmDocumentConfig:
    out: SsmDocumentConfig = {}  # type: ignore[typeddict-item]
    if data.get("crossAccountRole") is not None:
        out["cross_account_role"] = data["crossAccountRole"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("documentArn") is not None:
        out["document_arn"] = data["documentArn"]
    else:
        raise DeserializationError("SsmDocumentConfig.document_arn required")
    if data.get("targets") is not None:
        import capo_arc_region_switch.types.ssm_target_list

        out["targets"] = (
            capo_arc_region_switch.types.ssm_target_list.deserialize_aws_json_1_0(
                data["targets"]
            )
        )
    else:
        raise DeserializationError("SsmDocumentConfig.targets required")
    if data.get("parameters") is not None:
        import capo_arc_region_switch.types.ssm_document_parameters

        out["parameters"] = (
            capo_arc_region_switch.types.ssm_document_parameters.deserialize_aws_json_1_0(
                data["parameters"]
            )
        )
    if data.get("documentVersion") is not None:
        out["document_version"] = data["documentVersion"]
    return out

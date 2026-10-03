"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsLambdaLayerVersionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_lambda_layer_version_number
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.non_empty_string_list


class AwsLambdaLayerVersionDetails(TypedDict, closed=True):
    version: NotRequired[
        "capo_securityhub.types.aws_lambda_layer_version_number.AwsLambdaLayerVersionNumber"
    ]
    """<p>The version number.</p>"""
    compatible_runtimes: NotRequired[
        "capo_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The layer's compatible <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html">function runtimes</a>.</p> <p>The following list includes deprecated runtimes. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy">Runtime deprecation policy</a> in the <i>Lambda Developer Guide</i>.</p> <p>Array Members: Maximum number of 5 items.</p> <p>Valid Values: <code>nodejs | nodejs4.3 | nodejs6.10 | nodejs8.10 | nodejs10.x | nodejs12.x | nodejs14.x | nodejs16.x | java8 | java8.al2 | java11 | python2.7 | python3.6 | python3.7 | python3.8 | python3.9 | dotnetcore1.0 | dotnetcore2.0 | dotnetcore2.1 | dotnetcore3.1 | dotnet6 | nodejs4.3-edge | go1.x | ruby2.5 | ruby2.7 | provided | provided.al2 | nodejs18.x | python3.10 | java17 | ruby3.2 | python3.11 | nodejs20.x | provided.al2023 | python3.12 | java21</code> </p>"""
    created_date: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the version was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsLambdaLayerVersionDetails) -> dict:
    out: dict = {}
    if "version" in value:
        out["Version"] = value["version"]
    if "compatible_runtimes" in value:
        import capo_securityhub.types.non_empty_string_list

        out["CompatibleRuntimes"] = (
            capo_securityhub.types.non_empty_string_list.serialize_json(
                value["compatible_runtimes"]
            )
        )
    if "created_date" in value:
        out["CreatedDate"] = value["created_date"]
    return out


def deserialize_json(data: dict) -> AwsLambdaLayerVersionDetails:
    out: AwsLambdaLayerVersionDetails = {}  # type: ignore[typeddict-item]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("CompatibleRuntimes") is not None:
        import capo_securityhub.types.non_empty_string_list

        out["compatible_runtimes"] = (
            capo_securityhub.types.non_empty_string_list.deserialize_json(
                data["CompatibleRuntimes"]
            )
        )
    if data.get("CreatedDate") is not None:
        out["created_date"] = data["CreatedDate"]
    return out

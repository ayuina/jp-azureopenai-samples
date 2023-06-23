# coding: utf-8

"""
    Speech to Text API v3.0

    Speech to Text API v3.0.  # noqa: E501

    OpenAPI spec version: v3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class EndpointPropertiesUpdate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'content_logging_enabled': 'bool'
    }

    attribute_map = {
        'content_logging_enabled': 'contentLoggingEnabled'
    }

    def __init__(self, content_logging_enabled=None, _configuration=None):  # noqa: E501
        """EndpointPropertiesUpdate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._content_logging_enabled = None
        self.discriminator = None

        if content_logging_enabled is not None:
            self.content_logging_enabled = content_logging_enabled

    @property
    def content_logging_enabled(self):
        """Gets the content_logging_enabled of this EndpointPropertiesUpdate.  # noqa: E501

        A value indicating whether content logging (audio &amp; transcriptions)  is being used for a deployment.  # noqa: E501

        :return: The content_logging_enabled of this EndpointPropertiesUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._content_logging_enabled

    @content_logging_enabled.setter
    def content_logging_enabled(self, content_logging_enabled):
        """Sets the content_logging_enabled of this EndpointPropertiesUpdate.

        A value indicating whether content logging (audio &amp; transcriptions)  is being used for a deployment.  # noqa: E501

        :param content_logging_enabled: The content_logging_enabled of this EndpointPropertiesUpdate.  # noqa: E501
        :type: bool
        """

        self._content_logging_enabled = content_logging_enabled

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EndpointPropertiesUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EndpointPropertiesUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EndpointPropertiesUpdate):
            return True

        return self.to_dict() != other.to_dict()

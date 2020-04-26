package org.euvsvirus.entity;

import lombok.Data;

@Data
public class Attribute {
	public String attributeName;
	public String attributeType;

	public Attribute(String attributeName, String attributeType) {
		setAttributeName(attributeName);
		setAttributeType(attributeType);
	}
}

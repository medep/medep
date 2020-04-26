package org.euvsvirus.dao;

import java.util.List;

import org.euvsvirus.entity.Attribute;

import lombok.Data;

@Data
public class DataObject {

	public List<Attribute> attributes;
	public List<Object> data;
}

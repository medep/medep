package org.euvsvirus.entity;

import java.util.List;

import org.euvsvirus.dao.DataObject;

import lombok.Data;

@Data
public class Dataset {

	public Integer ID;
	public String datasetName;
	public List<String> authors;
	public List<String> owners;
	public DataObject data;
}

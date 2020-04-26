package org.euvsvirus.service;

import java.util.List;

import org.euvsvirus.entity.Dataset;

/**
 * This service interface is used to implement communication within
 * organization.
 * 
 * @author martinb
 *
 */
public interface LocalOrganizationService {
	
	/* Name of local endpoint; e.g. University Medical Centre Maribor, Slovenia*/
	String getEndpointName();
	
	/* Returns metadata about all available datasets. */
	List<Dataset> getAllData();
}

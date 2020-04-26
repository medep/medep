package org.euvsvirus;

import java.util.List;

import javax.annotation.PostConstruct;

import org.euvsvirus.connector.HospitalInformationSystem;
import org.euvsvirus.dao.DataObject;
import org.euvsvirus.entity.Dataset;
import org.euvsvirus.fake.FakeDataFactory;
import org.euvsvirus.service.LocalOrganizationService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * This is the root service. It communicates to all available adapters within
 * the organization.
 * 
 * @author martinb
 *
 */
@Service
public class UMCMService implements LocalOrganizationService {

	@Autowired
	List<HospitalInformationSystem> connectedSystems; // all connectors are available after startup

	@PostConstruct
	public void init() {
		// initialize and connect all connectors
		for (HospitalInformationSystem his : connectedSystems) {
			his.connect();
			System.out.println(his.whoami());
			System.out.println("Am I connected? => " + (his.isConnected() ? "Yes" : "No"));
		}
	}

	@Override
	public List<Dataset> getAllData() {
		List<Dataset> lst = FakeDataFactory.getAllMetadata();
		return lst;
	}

	@Override
	public String getEndpointName() {
		return "University Medical Centre Maribor, Slovenia";
	}
}

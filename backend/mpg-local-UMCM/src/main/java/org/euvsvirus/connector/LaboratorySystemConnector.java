package org.euvsvirus.connector;

import org.springframework.stereotype.Component;

@Component
public class LaboratorySystemConnector implements HospitalInformationSystem {

	boolean connected = false;

	@Override
	public void connect() {
		connected = true;
	}

	@Override
	public String whoami() {
		return "I am the Laboratory system connector. I connect to the laboratory information system and collect data from results of blood samples, various types of swabs, etc";
	}

	@Override
	public boolean isConnected() {
		return connected;
	}

}

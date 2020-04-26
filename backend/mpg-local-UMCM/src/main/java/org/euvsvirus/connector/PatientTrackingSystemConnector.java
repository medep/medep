package org.euvsvirus.connector;

import org.springframework.stereotype.Component;

@Component
public class PatientTrackingSystemConnector implements HospitalInformationSystem {

	boolean connected = false;
	
	@Override
	public void connect() {
		connected = true;		
	}

	@Override
	public boolean isConnected() {
		return connected;
	}
	@Override
	public String whoami() {
		return "I am Patient tracking system connector. I connect to the biggest information system in the hospital that tracks admissions and dismissals of patients along with electronic health records etc. It is possible, that hospitals have more than one such system!";
	}
}

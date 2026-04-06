import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";

const firebaseConfig = {
  apiKey: "AIzaSyAPG68rfy-L_MMy9rnnDtitQebHnQCmNc8",
  authDomain: "ransomware-simulator-d2074.firebaseapp.com",
  databaseURL: "https://ransomware-simulator-d2074-default-rtdb.firebaseio.com",
  projectId: "ransomware-simulator-d2074",
  storageBucket: "ransomware-simulator-d2074.firebasestorage.app",
  messagingSenderId: "875026460830",
  appId: "1:875026460830:web:8559b26922da53caf38b8f"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);

// EXPORT so other files can use it
export { auth, db };
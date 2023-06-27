import { useState } from "react";
import Image from 'next/image';
import SpeechRecognition, {useSpeechRecognition} from "react-speech-recognition";
import mic from '@/../public/assets/mic.png'
import api from "@/services/api";

export default function Speech({ id, refreshData, setIsOpen }) {
    const [isRecording, setIsRecording] = useState(false);
    const [actualConversation, setActualConversation] = useState("");
    const [messages, setMessages] = useState([]);

    const {
        transcript, 
        resetTranscript,
        browserSupportsSpeechRecognition
    } = useSpeechRecognition();

    if (!browserSupportsSpeechRecognition) return (<span>Seu navegador não é compativel com SpeechRecognition.</span>);

    const whenStopListening = async () => {
        SpeechRecognition.stopListening();
        let content = transcript;
        content = content[0].toUpperCase() + content.substring(1);
        await api.post("/sentimentAnalysis", {
            text: content
        }, { headers: {'company-id': id} })
        .then(result => {
            refreshData();
            setIsOpen(false);
        })
        .catch(error => console.error(error))
        setIsRecording(!isRecording);
        resetTranscript();
    }

    const toggleAudio = () => {
        if (isRecording) {
            whenStopListening();
        } else {
            resetTranscript();
            SpeechRecognition.startListening({continuous: true, language: 'pt-BR'});
            setIsRecording(!isRecording);
        }
    }

    const updateActualConversation = conversation => {
        setActualConversation(conversation);
    }

    const Footer = () => {
        return (
            <div className="footer">
                <button
                    className={`audioRecorder ${isRecording ? "audioRecording" : ""}`}
                    onClick={toggleAudio}
                >
                    <Image 
                        src={mic}
                        alt="MicImage"
                    />
                </button>
                {isRecording && <p>Listening...</p>}
            </div>
        )
    }

    return (
        <>
            <div className="main">
                {
                    messages?.length || isRecording ?
                    messages.map((message) => {
                        return (
                            <div key={message.id}>
                                <div className="divMessage">
                                    <p className="pMessage">{message.content}</p>
                                    <p className="pTime">{`${message.messageDate} ${message.messageTime}`}</p>
                                </div>
                            </div>
                        )
                    })
                    :
                    <div className="emptyMessages">
                        <h3>Aguardando inicio da simulação</h3>
                    </div>
                }
                {
                    transcript && isRecording &&
                    <div className="divMessage">
                        <p className="pMessage">{transcript}</p>
                    </div>
                }
            </div>
            <Footer />
        </>
    )
}
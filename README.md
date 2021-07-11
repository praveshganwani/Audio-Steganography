# Audio Steganography using RSA and ChaCha-20 Encryption Techniques

The proposed algorithm introduces a multilevel approach to the existing LSB encoding technique.

The proposed algorithm is designed to use stereo audio with WAV format sampled at any frequency. Using two different cryptography methods (one symmetric key and one public-key cryptography), the algorithm can enhance the security of the embedded data in the audio file.

The embedding algorithm is divided into four steps, and it takes place at the sender’s end. Below image shows all the steps involved in the embedding process. The presented technique utilizes ChaCha20 and RSA encryption algorithms to attain - (i) decent hiding quantity & (ii) improved security using a public key cryptosystem and a modified version of Least Significant Bit (LSB) encoding technique to embed the encrypted data in the cover audio file.
